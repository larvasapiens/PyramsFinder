#!python2
#  -*- coding: utf-8 -*-
#  PF_Tests.py
#  Author: Larvasapiens <sebasnr95@gmail.com>
#  Creation Date: 2016-01-21
#  Last Modification: 2016-01-21
#  Version: 1.0

from PyramsFinder import *

"""
Some tests for the PyramsFinder module.
"""

class C:
    
    def evalFuncParallel(self, maxTime, score):
        startTime = time.time()
        print("Starting countdown til {} mins have passed".format(maxTime))
        while(True):
            elapsedMinutes = (time.time() - startTime) * (1.0 / 60.0)
            if elapsedMinutes > maxTime:
                break
        print("{} mins passed".format(maxTime))
        
        return score
    

if __name__ == '__main__':
    c = C()
    
    def evalFunc(a, b):
        return a - b
    
    # Try to maximize the score. A score of 50 is good enough.
    paramsFinder = ParametersFinder(
        evalFunc, 
        (Parameter('b', 'int', value=50, minVal=0, maxVal=50, maxChange=5),),
        nonOptimParams={'a' : 70}
    )
    
    bestParameters = paramsFinder.findParams(
            populationSize=5,
            maxMutations=1,
            variety=2,
            elitism=1,
            selectionTechnique='RouletteWheel',
            randomizeFirstGen=True,
            maxIterations=-1,
            maxTime=-1,
            minScore=50,
            nParallelEvals=1,
            savingFrequency=2,
            verbosity=2
        )

    print("BEST FOUND:")
    print(bestParameters)
    
    
    paramsFinder = ParametersFinder(
        c.evalFuncParallel,
        (
            Parameter('maxTime', 'float', value=1, minVal=0, maxVal=5,
                maxChange=1),
            Parameter('score', 'int', minVal=0, maxVal=50, maxChange=5)
        ),
        isInstanceMethod=True
    )
    bestParameters = paramsFinder.findParams(
            populationSize=5,
            maxMutations=2,
            variety=2,
            elitism=1,
            selectionTechnique='RouletteWheel',
            randomizeFirstGen=True,
            maxIterations=10,
            maxTime=-1,
            minScore=50,
            nParallelEvals=2,
            savingFrequency=1,
            verbosity=2
        )

    print("BEST FOUND:")
    print(bestParameters)
