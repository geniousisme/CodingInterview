class TrieNode(object):
    def __init__(self):
        self.leaf = False
        self.children = {}


class IpFilter(object):
    def __init__(self, rules):
        self.root = IpFilter._build_trie(rules)

    @staticmethod
    def _build_trie(rules):
        root = TrieNode()
        for rule in rules:
            ip, length = rule.split('/')
            p = root
            for bit in IpFilter._ip_str_to_bin(ip)[:int(length)]:
                if bit not in p.children:
                    p.children[bit] = TrieNode()
                p = p.children[bit]
            p.leaf = True
        return root

    @staticmethod
    def _ip_str_to_bin(ip):
        return ''.join(bin(int(i))[2:].zfill(8) for i in ip.split('.'))

    def match(self, ip):
        """
        If ip matches the rules
        :return: Boolean value
        """
        p = self.root
        for bit in IpFilter._ip_str_to_bin(ip):
            if p.leaf:
                return True
            if bit not in p.children:
                return False
            p = p.children[bit]
        return False


ip_filter = IpFilter(["7.0.0.0/8", "208.130.28.0/22", "7.7.0.0/16"])
print ip_filter.match("7.0.0.0")
print ip_filter.match("7.0.0.234")
print ip_filter.match("6.1.0.234")

print ip_filter.match("208.130.29.90")