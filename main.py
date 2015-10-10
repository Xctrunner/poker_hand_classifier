import neural_net
import importcsv as icsv

def run():
    ## inputs = csv.open_card_csv('train.csv')
    ## #numbers hardcoded for now, and no functions specified
    ## out_node = Node(f)
    ## mid_layer1 = Layer(f_list1)
    ## mid_layer2 = Layer(f_list2)
    ## mid_layers = [mid_layer1,mid_layer2]
    ## network = Network(5,mid_layers,out_node)
    ## network = network.add_edges

    ## alg.train(inputs,network,10000)

    ## network.print_weights
    ## return
    t,v,r = icsv.csv_to_binary('train.csv')
    network = neural_net.Net([52,30,10])
    network.SGD(t,30,10,3.0,test_data=r)

run()    
