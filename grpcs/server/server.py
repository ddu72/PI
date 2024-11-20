from concurrent import futures
import grpc
import tts_pb2
import tts_pb2_grpc
from TTS.api import TTS  # Coqui TTS
import numpy as np
import traceback

class TTSService(tts_pb2_grpc.TTSServiceServicer):
    def __init__(self):
        print("Loading TTS model...")
        # Use a faster TTS model if possible
        self.tts = TTS(model_name="tts_models/en/ljspeech/fast_pitch")
        print("TTS model loaded successfully!")
        
    def SynthesizeStream(self, request_iterator, context):
        chunk_index = 0
        block_size = 8192  # Increased block size for efficiency

        for request in request_iterator:
            text = request.text
            print(f"Received text to synthesize: {text}")

            try:
                # Generate audio
                audio = self.tts.tts(text)
                # Ensure the audio is in [-1.0, 1.0]
                audio = np.clip(audio, -1.0, 1.0)
                # Convert to 16-bit PCM
                audio = np.int16(audio * 32767)
                print(f"Audio generated successfully. Total samples: {len(audio)}")

                # Stream audio in chunks
                for i in range(0, len(audio), block_size):
                    audio_chunk = audio[i:i + block_size]
                    yield tts_pb2.SynthesisResponse(
                        audio_chunk=audio_chunk.tobytes(),
                        chunk_index=chunk_index
                    )
                    chunk_index += 1
            except Exception as e:
                # Log the full traceback of the error
                print(f"Error generating audio: {e}")
                traceback.print_exc()
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.INTERNAL)
                break

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))  # Scalable server
    tts_pb2_grpc.add_TTSServiceServicer_to_server(TTSService(), server)
    server.add_insecure_port('[::]:50051')
    print("TTS server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
