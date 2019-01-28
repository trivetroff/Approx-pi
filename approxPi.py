import argparse
import math

from src import myClass
from src.myClass import PiMethodes
from src.myClass import Graph
from src.myClass import Data


#Tools functions:
def roundNumber(number, precision):
    return math.floor(number * (math.pow(10, precision))) / (math.pow(10, precision))


#Main functions
def gen_pi(args):
    engine = PiMethodes()
    if args.method == '1':
        print(engine.MethodeSerieInvCarres(args.depth))
    elif args.method == '2':
        print (engine.MethodeSerieInvCarresImparis(args.depth))
    elif args.method == '3':
        print (engine.MethodeSerieRamanujan(args.depth))

def displayGraphCompareMethods(args):
    engine = PiMethodes()
    view = Graph()
    result_invCarres = []
    result_invCarresImparis = []
    for k in range (0, args.depth):
        result_invCarres.append(abs(engine.MethodeSerieInvCarres(k) - engine.realPi()))
        result_invCarresImparis.append(abs(engine.MethodeSerieInvCarresImparis(k) - engine.realPi()))
    view.addData(Data(result_invCarres, label='MethodeSerieInvCarres')) \
        .addData(Data(result_invCarresImparis, label='MethodeSerieInvCarresImparis')) \
        .showLegend() \
        .view()

def estimatePi(args):
    engine = PiMethodes()
    pi = engine.realPi()
    pi = roundNumber(pi, args.precision)
    estimation = 0
    depth = 0
    while not roundNumber(estimation, args.precision) == pi:
        depth +=1
        if (args.method == '1'):
            estimation = engine.MethodeSerieInvCarres(depth)
        elif (args.method == '2'):
            estimation = engine.MethodeSerieInvCarresImparis(depth)
        elif (args.method == '3'):
            estimation = engine.MethodeSerieRamanujan(depth)
    print("Result :" + str(depth))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='cmd')
    subparser.required = True

    #Generation of pi parse
    genpi_pars = subparser.add_parser('genpi', help='Generate pi')
    genpi_pars.add_argument("--method", help="Choose the method (normal(1), imparis(2), ramanujan(3))", type=str, default='1')
    genpi_pars.add_argument("depth", help="Depth of sum", type=int)
    genpi_pars.set_defaults(func=gen_pi)

    #Generation of comparative graph
    compGraph_pars = subparser.add_parser('compgraph', help='Generate pi')
    compGraph_pars.add_argument("depth", help="Depth of sum", type=int)
    compGraph_pars.set_defaults(func=displayGraphCompareMethods)

    #Generation of findpi parse
    findpi_pars = subparser.add_parser('estimatepi', help='Find index for which pi is estimated with a good precision')
    findpi_pars.add_argument("precision", help="Precision of pi", type=int)
    findpi_pars.add_argument("--method", help="Choose the method (normal(1), imparis(2), ramanujan(3))", type=str, default='1')
    findpi_pars.set_defaults(func=estimatePi)

    args = parser.parse_args()
    print(args)
    args.func(args)
