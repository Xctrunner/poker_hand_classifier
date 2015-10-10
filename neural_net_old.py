class Edge:
    def __init__(self,above,below,weight):
        self.above = above
        self.below = below
        self.weight = weight

class Node:
    def __init__(self,func):
        self.edges_above = []
        self.edges_below = []
        self.function_choice = func
        self.function = None

    # add the edges going to the layer above to the node
    def add_edges_above(self,nodes_above):
        for node in nodes_above:
            self.edges_above.append(Edge(node,self,0))

    # add the edges going to the layer below to the node
    def add_edges_below(self,nodes_below):
        for node in nodes_below:
            self.edges_below.append(Edge(self,node,0))

    # assigns the actual function to the node instead of a string representing the function
    def choose_func(self,f_choice):
        #example
        if f_choice == "sig":
            self.function = "sigmoid function" # actual sigmoid function
        # add other cases


    # calculate the input to the node based on the outputs of nodes below and the weights of
    # their edges to this node
    def calc_input(self):
        e = self.edges_below
        sum_below = 0
        for edge in e:
            sum_below += (edge.below.out * edge.weight)
        return sum_below

    # apply the node's function to an input float (return another float)
    def calc_output(self):
        return self.function(self.calc_input)

# a layer is a list of nodes; may have other properties in futures as this doesn't seem totally # necessary at the moment
class Layer:
    def __init__(self,nodes):
        self.nodes = nodes

class Network:
    def __init__(self,inputs,mid_layers,out_node):
        self.inputs = inputs
        self.mid_layers = mid_layers
        self.out_node = out_node

    # calculate the result of a single input (one hand, in this case) being passed into the
    # function
    def input(self,ins):
        
        return

    # given a network of layers of edgeless nodes, add all of the edges to each node
    # here, they will each be given weight zero
    def add_edges(self):
        if len(self.mid_layers) < 1:
            for inp in self.inputs:
                inp.edges_above.append(Edge(self.out_node,inp,0))
                self.out_node.edges_below.append(Edge(self.out_node,inp,0))
        else:
            for inp in self.inputs:
                add_edges_above(self.mid_layers[0])
                for node in self.mid_layers[0]:
                    node.edges_below.append(Edge(node,inp,0))
            self.out_node.add_edges_below(self.mid_layers[-1])
            for node in self.mid_layers[-1]:
                node.edges_above.append(Edge(self.out_node,node,0))
            if len(mid_layers) > 1:
                for i in range(len(self.mid_layers)-1):
                    for node in self.mid_layers[i]:
                        node.add_edges_above(self.mid_layers[i+1])
                for j in range(1,len(self.mid_layers)):
                    for node in self.mid_layers[j]:
                        node.add_edges_below(self.mid_layers[j-1])


    # print out the weights in a meaningful way such as "A1B1 = .703, A1B2 = .193"
    def print_weights(self):
        if len(self.mid_layers) < 1:
            for i in range(self.inputs):
                print("Weight of input "+i+" to output is: "+
                      self.inputs[i].edges_above[0].weight)
        else:
            for i in range(self.inputs):
                for edge in self.inputs[i].edges_above:
                    print("Weight of input "+i+" to function \""
                          +edge.above.function_choice+"\" in hidden layer 1 is: "+edge.weight)
            for j in range(self.mid_layers-1):
                for node in self.mid_layers[j]:
                    for edge in node.edges_above:
                        print("Weight of output of \""+node.function_choice
                              +"\" in hidden layer "+j+" to function \""
                              +edge.above.function_choice+"\" in hidden layer "+(j+1)+" is: "
                              +edge.weight)
            for k in range(self.mid_layers[-1]):
                print("Weight of output of \""+self.mid_layers[-1][k].function_choice
                      +"\" in hidden layer "+len(mid_layers)-1+" to output node is: "
                      +self.mid_layers[-1][k].edges_above[0].weight)
        
