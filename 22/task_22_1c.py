topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self,topology_dict):
        result = {}
        for key, value in topology_dict.items():
            if not topology_dict.get(value) == key:
                result[key] =  value
        return result
    
    def delete_link(self, start, end):
        if self.topology.get(start) == end:
            del self.topology[start]
        elif self.topology.get(end) == start:
            del self.topology[end]
        else:
            print("Такого соединения нет")

    def delete_node(self, node):

        checker = 0
        for x, y in list(self.topology.items()):
            if node in x or node in y:
                del self.topology[x]
                checker =1
        if checker == 0:
            print("Такого устройства нет")

top = Topology(topology_example)
print(top.topology)

top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
print(top.topology)

top.delete_node('SW1')
print(top.topology)