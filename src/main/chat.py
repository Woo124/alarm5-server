

class ChatRoom(dict):
    """ Chat Room Class
    key: user id
    value: message list
    """

    def send_message(self, to: str, message: str):
        """ Send Chat Message to User
        :param to: str
        :param message: str
        :returns: None
        """
        if to not in self:
            self[to] = []
        self[to].append(message)

    def recv_message(self, user: str):
        """ Receive Chat Message from User
        :param user: str
        :returns: str
        """
        return self.pop(user, [])
