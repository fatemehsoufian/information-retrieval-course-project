INPUT_FILE = '/Users/fatemehsoufian/Desktop/examples/smallrmat.dat'
OUTPUT_FILE = '/Users/fatemehsoufian/Desktop/pagerank.txt'
NUM_ITERATIONS = 10


class DirectedGraph:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def page_rank(self, num_iterations=NUM_ITERATIONS, damping_factor=0.85):
        pagerank = [1/self.num_nodes] * self.num_nodes
        for i in range(num_iterations):
            new_pagerank = [0] * self.num_nodes
            for u in range(self.num_nodes):
                for v in self.adj_list[u]:
                    new_pagerank[v] += damping_factor * \
                        pagerank[u] / len(self.adj_list[u])
                new_pagerank[u] += (1 - damping_factor) / self.num_nodes
            pagerank = new_pagerank

            # create a new file for writing
            with open(OUTPUT_FILE, 'a') as f:
                f.write('Iteration {}\n'.format(i+1))
                for u in range(self.num_nodes):
                    f.write('Node {}: PageRank = {:.10f}\n'.format(
                        u, pagerank[u]))

        return pagerank


with open(INPUT_FILE, 'r') as f:
    num_nodes = int(f.readline().strip())
    num_edges = int(f.readline().strip())

    graph = DirectedGraph(num_nodes)

    for i in range(num_edges):
        line = f.readline().strip().split()
        u, v = int(line[0]), int(line[1])
        graph.add_edge(u, v)

    # compute the PageRank values for the graph
    pagerank = graph.page_rank(num_iterations=NUM_ITERATIONS)

    with open(OUTPUT_FILE, 'a') as f:
        f.write('Final PageRank values:\n')
        for u in range(num_nodes):
            print("Node {}: PageRank = {:.10f}".format(u, pagerank[u]))
            f.write("Node {}: PageRank = {:.10f}\n".format(u, pagerank[u]))

    print('PageRank values saved to {}'.format(OUTPUT_FILE))
