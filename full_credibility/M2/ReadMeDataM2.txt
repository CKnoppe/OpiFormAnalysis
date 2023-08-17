This file contains meta information about simulations.

M2: MODEL VERSION 2
    • Matching: sentiments bound alpha; opinion difference; credibility score (kappa)
    • Opinion update: Standard model with credibility bound (theta; gamma)

Folder's Names: [K1G1T1][A300][T1000][M:[0.5:0.95]][s: values from 5 to 95]-[n8]

K0: credibility in matching
G0: credibility in the opinion update
T1: standard model with tolerance theta in the opinion update
A: number of agents in the treatment
T: number of simulations in the treatment
M: a mean value \mu(\lambda) of the bounded confidence parameter \lambda in the treatment
    \lambda of each agent is drawn from the normal distribution 
    (see Table 2 in the paper for more details)
s: a number of hundreths of the upper sentiment bound per each treatment, i.e. "5 -> \alpha = 0.05"
    (see Table 2 in the paper for more details about the parameters for sentiments)
n8: expected number of direct neighbours in the SW network (after rewiring # of neighbors will differ from agent to agent)

File names: 

agents_init - IGNORE THESE VALUES. 
The file includes two columns: 
            1. column: initial age of agent before the launch
            2. column: initial opinion x_i before the launch

Network.txt: file includes the SW networks on which treatments were performed
             (the same for all treatments to ensure cross comparisons / repetitions)

results_SB_(0->1000): opinions of agents at particular T:
                      11 files for 11 different points in T, s.t.
                      T={0,100,200,...,1000}
                      These files include the same type of information as in the file agents_init.txt
	              
           Each line shows age and opinion for each agent within the treatment (i.e. the folder name)
           1. line: agent 1; treatment \mu(\theta)=0.1; \mu(\gamma)=0.1; \mu(\kappa)=0.1
           2. line: agent 2; treatment \mu(\theta)=0.1; \mu(\gamma)=0.1; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
	   300. line: agent 300; treatment \mu(\theta)=0.1; \mu(\gamma)=0.1; \mu(\kappa)=0.1

	   301. line: agent 1; treatment \mu(\theta)=0.2; \mu(\gamma)=0.1; \mu(\kappa)=0.1
           302. line: agent 2: treatment \mu(\theta)=0.2; \mu(\gamma)=0.1; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
           600. line: agent 300; treatment \mu(\theta)=0.2; \mu(\gamma)=0.1; \mu(\kappa)=0.1

           601. line: agent 1; treatment \mu(\theta)=0.3; \mu(\gamma)=0.1; \mu(\kappa)=0.1
           602. line: agent 2; treatment \mu(\theta)=0.3; \mu(\gamma)=0.1; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
           900. line: agent 300; treatment \mu(\theta)=0.3; \mu(\gamma)=0.1; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **

          3001. line: agent 1; treatment \mu(\theta)=0.1; \mu(\gamma)=0.2; \mu(\kappa)=0.1
          3002. line: agent 2; treatment \mu(\theta)=0.1; \mu(\gamma)=0.2; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
	  3300. line: agent 300; treatment \mu(\theta)=0.1; \mu(\gamma)=0.2; \mu(\kappa)=0.1

	  3301. line: agent 1; treatment \mu(\theta)=0.2; \mu(\gamma)=0.2; \mu(\kappa)=0.1
	  3302. line: agent 2; treatment \mu(\theta)=0.2; \mu(\gamma)=0.2; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
	  3600. line: agent 300; treatment \mu(\theta)=0.2; \mu(\gamma)=0.2; \mu(\kappa)=0.1

	  3601. line: agent 1; treatment \mu(\theta)=0.3; \mu(\gamma)=0.2; \mu(\kappa)=0.1
	  3602. line: agent 2; treatment \mu(\theta)=0.3; \mu(\gamma)=0.2; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **

          218401. line: agent 1; treatment \mu(\theta)=0.9; \mu(\gamma)=0.9; \mu(\kappa)=0.9
          218402. line: agent 2; treatment \mu(\theta)=0.9; \mu(\gamma)=0.9; \mu(\kappa)=0.9
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
          218700. line: agent 300; treatment \mu(\theta)=0.9; \mu(\gamma)=0.9; \mu(\kappa)=0.9

           File includes these 2 columns:
            1. column: - age og agent (ignore this column) -
            2. column: opinion of agent at time T in a given treatment (see T from the file name)


stats.txt: some statistical data for each simulation treatment (collected at T=1000).
           Each line shows a separate scenario within the main treatment (i.e. the folder name)
           1. line: \mu(\theta)=0.1; \mu(\gamma)=0.1; \mu(\kappa)=0.1
           2. line: \mu(\theta)=0.2; \mu(\gamma)=0.1; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
          10. line: \mu(\theta)=0.1; \mu(\gamma)=0.2; \mu(\kappa)=0.1
          11. line: \mu(\theta)=0.2; \mu(\gamma)=0.2; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
          19. line: \mu(\theta)=0.1; \mu(\gamma)=0.3; \mu(\kappa)=0.1
          20. line: \mu(\theta)=0.2; \mu(\gamma)=0.3; \mu(\kappa)=0.1
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
          82. line: \mu(\theta)=0.1; \mu(\gamma)=0.1; \mu(\kappa)=0.2
          83. line: \mu(\theta)=0.2; \mu(\gamma)=0.1; \mu(\kappa)=0.2
                 **                  **                  **
                 **                  **                  **
                 **                  **                  **
         728. line: \mu(\theta)=0.8; \mu(\gamma)=0.9; \mu(\kappa)=0.9
         729. line: \mu(\theta)=0.9; \mu(\gamma)=0.9; \mu(\kappa)=0.9

           File includes these 6 columns:
            1. column: - ignore this column -
            2. column: mean opinion of all agents
            3. column: variance in opinion of all agents
            4. column: number of meetings of all agents
            5. column: number of opinion changes of all agents
            6. column: net opinion change (sum of all opinion changes throughout the treatment
                       -> note that initial opinions are normally distributed N(0,0.5))

stats_indv.txt: statistical data for pairwise meetings (collected at T=1000).
            1. column: agent’s ID
            2. column: agent’s neighbors IDs
            3. column: number of meetings between agent and its neighbor
            4. column: number of opinion changes in meetings between agent and its neighbor
            5. column: overall net opinion change from meetings between agent and its neighbor 