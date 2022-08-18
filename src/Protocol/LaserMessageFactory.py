from Protocol.Messages.Client.Other.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.Authentication.LoginMessage import LoginMessage
from Protocol.Messages.Client.Battle.StartGameMessage import StartGameMessage
from Protocol.Messages.Client.Battle.CancelMatchmakingMessage import CancelMatchmakingMessage
from Protocol.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Protocol.Messages.Client.Team.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.Home.EndClientTurnMessage import EndClientTurnMessage


packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    14102: EndClientTurnMessage,
    14103: StartGameMessage,
    14106: CancelMatchmakingMessage,
    14113: GetPlayerProfileMessage,
    14350: TeamCreateMessage,
}
