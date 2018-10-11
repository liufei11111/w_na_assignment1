import snap
import numpy as np
import matplotlib.pyplot as plt

def load_graph(name):
    '''
    Helper function to load graphs.
    Wse "epinions" for Epinions graph and "email" for Email graph.
    Check that the respective .txt files are in the same folder as this script;
    if not, change the paths below as required.
    '''
    if name == "epinions":
        G = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1)
    elif name == 'email':
        G = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1)   
    else: 
        raise ValueError("Invalid graph: please use 'email' or 'epinions'.")
    return G

def q2_1():
    '''
    You will have to run the inward and outward BFS trees for the 
    respective nodes and reason about whether they are in SCC, IN or OUT.
    You may find the SNAP function GetBfsTree() to be useful here.
    '''
    
    ##########################################################################
    #TODO: Run outward and inward BFS trees from node 2018, compare sizes 
    #and comment on where node 2018 lies.
    G = load_graph("email")
    #Your code here:
    outward_set = set()
    BfsTree = snap.GetBfsTree(G, 2018, True, False)
    for EI in BfsTree.Edges():
        outward_set.add(EI.GetDstNId())
        # print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())
    inward_set = set()
    BfsTree = snap.GetBfsTree(G, 2018, False, True)
    for EI in BfsTree.Edges():
        inward_set.add(EI.GetDstNId())
        # print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())
    print('inward_set', len(inward_set))
    print('outward_set', len(outward_set))
    print('G size', G.GetEdges())
    MxScc = snap.GetMxScc(G)
    mxSccSize = MxScc.GetNodes()
    print 'SCC size:', mxSccSize
    print 'Relative size of SCC in Directed Graph:', snap.GetMxSccSz(G)
    
    
    ##########################################################################
    
    ##########################################################################
    #TODO: Run outward and inward BFS trees from node 224, compare sizes 
    #and comment on where node 224 lies.
    G = load_graph("epinions")
    #Your code here:
        #Your code here:
    outward_set = set()
    BfsTree = snap.GetBfsTree(G, 224, True, False)
    for EI in BfsTree.Edges():
        outward_set.add(EI.GetDstNId())
        # print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())
    inward_set = set()
    BfsTree = snap.GetBfsTree(G, 224, False, True)
    for EI in BfsTree.Edges():
        inward_set.add(EI.GetDstNId())
        # print "Edge from %d to %d in generated tree." % (EI.GetSrcNId(), EI.GetDstNId())
    print('inward_set', len(inward_set))
    print('outward_set', len(outward_set))
    print('G size', G.GetEdges())
    print 'Relative size of SCC in Directed Graph:', snap.GetMxSccSz(G)
    
    
    
    
    
    ##########################################################################

    print '2.1: Done!\n'

def q2_2_util(dataset_name, outward):
    G = load_graph(dataset_name)
    Rnd = snap.TRnd(42)
    Rnd.Randomize()
    rand_ids = set()
    while(len(rand_ids)<100):
        NId = G.GetRndNId(Rnd)
        rand_ids.add(NId)
    
    cumulative_list = []
    for rand_nid in rand_ids:
        if outward:
            BfsTree = snap.GetBfsTree(G, rand_nid, True, False)
        else:
            BfsTree = snap.GetBfsTree(G, rand_nid, False, True)
        outward_set = set()
        for EI in BfsTree.Edges():
            outward_set.add(EI.GetDstNId())
        cumulative_list.append(len(outward_set))
        # print(len(cumulative_list))
    x = np.linspace(0, 1, 100)
    # print(x)
    cumulative_list.sort()
    cumulative_list = np.array(cumulative_list)
    # print(cumulative_list)
    plt.plot(x, cumulative_list, lw=2)
    plt.legend()
    plt.xlabel('Frac of rand ids')
    plt.ylabel('%s Reached notes (%s)' % (dataset_name, 'outward' if outward else 'inward'))
    plt.yscale('log')
    plt.show()
def q2_2():
    '''
    For each graph, get 100 random nodes and find the number of nodes in their
    inward and outward BFS trees starting from each node. Plot the cumulative
    number of nodes reached in the BFS runs, similar to the graph shown in 
    Broder et al. (see Figure in handout). You will need to have 4 figures,
    one each for the inward and outward BFS for each of email and epinions.
    
    Note: You may find the SNAP function GetRndNId() useful to get random
    node IDs (for initializing BFS).
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:



    q2_2_util("email", True)
    q2_2_util("email", False)
    # TWO MORE
    q2_2_util("epinions", True)
    q2_2_util("epinions", False)




    
    
    
    
    
    
    
    
    ##########################################################################
    print '2.2: Done!\n'
def q2_3_util(dataset_name):
        # G = load_graph("email")
    G = load_graph(dataset_name)
    MxWcc = snap.GetMxWcc(G)
    total_size = G.GetNodes()
    wcc_size = MxWcc.GetNodes()
    disconnected_size = total_size - wcc_size
    print 'Total size: ', total_size
    print 'WCC size: ', wcc_size
    print 'DISCONNECTED: ', disconnected_size
    Rnd = snap.TRnd(42)
    Rnd.Randomize()
    MxScc = snap.GetMxScc(G)
    scc_size = MxScc.GetNodes()
    number_of_trials = 1
    scc_plus_out = 0
    scc_plus_in = 0
    out_size = 0
    in_size = 0
    tendrils_plus_tubes = 0
    for i in xrange(number_of_trials):
        NId = MxScc.GetRndNId(Rnd)
        # print 'Random node id', NId
        outward_set = set()
        BfsTree = snap.GetBfsTree(G, NId, True, False)
        for EI in BfsTree.Edges():
            outward_set.add(EI.GetDstNId())
        scc_plus_out = max(scc_plus_out, len(outward_set))
        out_size = max( out_size, scc_plus_out - scc_size)
        #
        inward_set = set()
        BfsTree = snap.GetBfsTree(G, NId, False, True)
        for EI in BfsTree.Edges():
            inward_set.add(EI.GetDstNId())
        scc_plus_in = max(scc_plus_in, len(inward_set))
        in_size = max(in_size, scc_plus_in - scc_size)
        tendrils_plus_tubes = max(tendrils_plus_tubes, wcc_size - in_size - out_size)

    print 'IN: ', in_size
    print 'scc_size', scc_size
    print 'scc + out: ', scc_plus_out
    print 'OUT: ', out_size
    print 'scc + in: ', scc_plus_in
    print 'TENDRILS + TUBES', tendrils_plus_tubes
    print '------------------'
def q2_3():
    '''
    For each graph, determine the size of the following regions:
        DISCONNECTED
        IN
        OUT
        SCC
        TENDRILS + TUBES
        
    You can use SNAP functions GetMxWcc() and GetMxScc() to get the sizes of 
    the largest WCC and SCC on each graph. 
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:
    # emails
    q2_3_util("email")
    q2_3_util("epinions")
    
    
    
    
    
    
    
    ##########################################################################
    print '2.3: Done!\n' 
def q2_4_utils(dataset_name):
    G = load_graph(dataset_name)
    Rnd = snap.TRnd(42)
    Rnd.Randomize()
    count = 0
    positive_count = 0
    negative_count = 0
    while count < 1000:
        NId_src = G.GetRndNId(Rnd)
        NId_dst = G.GetRndNId(Rnd)
        if NId_src != NId_dst:
            if snap.GetShortPath(G, NId_src, NId_dst, True) > 0:
                positive_count = positive_count + 1
            else:
                negative_count = negative_count + 1
        count = count + 1
            # print (snap.GetShortPath(G, NId_src, NId_dst))
    print 'positive_count', positive_count
    print 'negative_count', negative_count
def q2_4():
    '''
    For each graph, calculate the probability that a path exists between
    two nodes chosen uniformly from the overall graph.
    You can do this by choosing a large number of pairs of random nodes
    and calculating the fraction of these pairs which are connected.
    The following SNAP functions may be of help: GetRndNId(), GetShortPath()
    '''
    ##########################################################################
    #TODO: See above.
    #Your code here:

    q2_4_utils("email")
    
    q2_4_utils("epinions")
    
    
    
    ##########################################################################
    print '2.4: Done!\n'
    
if __name__ == "__main__":
    # q2_1()
    q2_2()
    # q2_3()
    # q2_4()
    print "Done with Question 2!\n"