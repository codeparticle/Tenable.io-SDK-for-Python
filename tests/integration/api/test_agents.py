from tenable_io.api.models import Agent, AgentList
from tenable_io.exceptions import TenableIOApiException, TenableIOErrorCode

from tests.base import BaseTest


class TestAgentsApi(BaseTest):

    def test_delete(self, client):
        try:
            client.agents_api.delete('test_agents_delete')
        except TenableIOApiException as e:
            assert e.code is TenableIOErrorCode.BAD_REQUEST, u'Bad request for string agent_id.'

    def test_list(self, client):
        agent_list = client.agents_api.list()
        assert isinstance(agent_list, AgentList)

        for a in agent_list.agents:
            assert isinstance(a, Agent)
