from Protocol.Messages.Client.Security.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.Authentication.LoginMessage import LoginMessage

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
}
