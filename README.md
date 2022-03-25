This repo contains:

1. Input data representing all possible match positions for a single player (startingconditions.csv)
2. A Python script which ingests the match positions and calculates the probability the player wins, loses, and ties the match
3. Output data from the script (probabilities.csv)

The script assumes each golf hole is an independent event where P(win hole) = P(lose hole) = .29 and P (tie hole) =  .42. This is based on a simple analysis of match data found at this link: https://toddwschneider.com/posts/how-many-paths-are-possible-in-an-18-hole-round-of-match-play-golf/.

The script uses recursion to calculate the probability of match outcomes given initial conditions. The following setup is used as a basis for the calcuation:

Let p(N,X) be the probability that player A eventually wins, given current state (N,X) where N represents their current point total (wins = 1, ties = .5, losses = 0), and X represents the number of holes remaining in the match. We have p(N,X) = 1 if N >= 9.5 and p(N,X) = 0 if N + X <= 9. By conditioning on the next hole, we obtain recursion:

    p(N,X) = p(N+1,X−1)ℙ(𝑊)+p(N,X−1)ℙ(T)+p(N−1,X−1)ℙ(L)
