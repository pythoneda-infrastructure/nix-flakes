from PythonEDA.event import Event
from PythonEDAInfrastructure.network.grpc.server import GrpcServer
from PythonEDANixFlakes.flake_requested import FlakeRequested

import logging

class NixFlakesGrpcServer(GrpcServer):

    async def FlakeRequestedNotifications(self, request, context):
        logging.getLogger(__name__).debug(f'Received "{request}", "{context}"')
#        response = flake_requested_pb2.Reply(code=200)
        event = self.build_flake_requested(request)
        await self.app.accept(event)
        return response

    async def add_servicers(self, server, app):
        # TODO: flake_requested_pb2_grpc.add_FlakeRequestedServiceServicer_to_server(self, server)
        pass
#
    def build_flake_requested(self, request) -> Event:
        return FlakeRequested(request.package_name, request.package_version)
