Rebound Height
Daniel has a ball. He wants to find the ball's rebound height, which he dropped from height H with an initial velocity V. After the Nth rebound the final velocity of the ball is
Vn. Your task is to help him find and return an integer value representing the height to which the ball rebounds after N bounces.
Note:
• H° = H *e^2n, where H" is the rebound height. H is the intiol height ea the coefficient of restitution and is the number of bounces
• e = V/Vn. where V is the initial velocity and V. is the final melbaty

Hn=H×e^2N
Where: Hn is the rebound height after N-th bounce.
H is the initial height.
e is the coefficient of restitution, calculated as e= V/vn where V is the initial velocity, and Vn is the velocity after N-th bounce.
N is the number of bounces.

Example

  H = 10 
  V= 15 
  Vn= 5 
  N= 3
Output= 7290




def rebound_height(H, V, Vn,N):
    e = V / Vn
    en = e ** (2*N)
    rebound_height = H * en
    return int(rebound_height)
H = 10  
V = 15  
Vn = 5 
N = 3
print(rebound_height(H, V, Vn,N))
