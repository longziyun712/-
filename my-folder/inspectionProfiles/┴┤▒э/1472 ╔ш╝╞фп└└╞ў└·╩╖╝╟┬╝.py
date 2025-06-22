class Listnode:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Listnode(homepage)

    def visit(self, url: str) -> None:
        nd = Listnode(url)
        self.current.next = nd
        nd.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current and steps:
            if self.current.prev == None:
                break
            self.current = self.current.prev
            steps -= 1

        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current and steps:
            if self.current.next == None:
                break
            self.current = self.current.next
            steps -= 1

        return self.current.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


