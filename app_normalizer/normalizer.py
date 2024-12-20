from concurrent import futures
import os
import sys
import argparse as ap
import grpc


from dotenv import load_dotenv
load_dotenv()  # Load environment variables from a .env file

## Load the proxy port from the environment variables
NORMALIZER_SERVICE_PORT = os.getenv("NORMALIZER_SERVICE_PORT")
if NORMALIZER_SERVICE_PORT is None:
    NORMALIZER_SERVICE_PORT = 50053 # Default port if not specified as an environment variable

NORMALIZER_SERVICE_RULES = os.getenv("NORMALIZER_SERVICE_RULES")
if NORMALIZER_SERVICE_RULES is None:
    NORMALIZER_SERVICE_RULES = "config/normalization/rules.toml" # Default rules file if not specified as an environment variable

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grpcs'))) # Add the grpcs directory to the system path
from grpcs import normalizer_pb2, normalizer_pb2_grpc
from __init__ import Normalizer

class NormalizerService(normalizer_pb2_grpc.NormalizerServiceServicer):
    def __init__(self, args):
        if args.rules is None:
            args.rules = NORMALIZER_SERVICE_RULES
        self.normalizer = Normalizer(args.rules)
        
    def Normalize(self, request, context):
        normalized_text = self.normalizer.normalize_text(request.text.strip())  # Normalization
        return normalizer_pb2.NormalizeResponse(normalized_text=normalized_text)

def serve(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    normalizer_pb2_grpc.add_NormalizerServiceServicer_to_server(NormalizerService(args), server)
    server.add_insecure_port(f'[::]:{NORMALIZER_SERVICE_PORT}')
    print(f"Normalizer server running on port {NORMALIZER_SERVICE_PORT}...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()