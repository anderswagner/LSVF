GT_FILENAME = "./Queries/10k-truth-to-100k-data.h5"
DS_FILENAME = "./Datasets/laion2B-en-hammingv2-n=100K.h5"
Q_FILENAME = "./Queries/public-queries-10k-hammingv2.h5"

NN = 10
P = 5
Q = 10000
K_INC = 1
K_START = 14
LSHBS_ENABLED = True
LSHDS_ENABLED = True
LSVF_ENABLED = True

LSHBS_TEXT = """
 /$$        /$$$$$$  /$$   /$$       /$$$$$$$  /$$   /$$            /$$$$$$                                    /$$ /$$                    
| $$       /$$__  $$| $$  | $$      | $$__  $$|__/  | $$           /$$__  $$                                  | $$|__/                    
| $$      | $$  \__/| $$  | $$      | $$  \ $$ /$$ /$$$$$$        | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$ 
| $$      |  $$$$$$ | $$$$$$$$      | $$$$$$$ | $$|_  $$_/        |  $$$$$$  |____  $$| $$_  $$_  $$ /$$__  $$| $$| $$| $$__  $$ /$$__  $$
| $$       \____  $$| $$__  $$      | $$__  $$| $$  | $$           \____  $$  /$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$| $$| $$  \ $$| $$  \ $$
| $$       /$$  \ $$| $$  | $$      | $$  \ $$| $$  | $$ /$$       /$$  \ $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$| $$| $$  | $$| $$  | $$
| $$$$$$$$|  $$$$$$/| $$  | $$      | $$$$$$$/| $$  |  $$$$/      |  $$$$$$/|  $$$$$$$| $$ | $$ | $$| $$$$$$$/| $$| $$| $$  | $$|  $$$$$$$
|________/ \______/ |__/  |__/      |_______/ |__/   \___/         \______/  \_______/|__/ |__/ |__/| $$____/ |__/|__/|__/  |__/ \____  $$
                                                                                                    | $$                         /$$  \ $$
                                                                                                    | $$                        |  $$$$$$/
                                                                                                    |__/                         \______/ 
"""

LSHDS_TEXT = """
 /$$        /$$$$$$  /$$   /$$       /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$
| $$       /$$__  $$| $$  | $$      | $$__  $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$$ | $$ /$$__  $$| $$_____/
| $$      | $$  \__/| $$  | $$      | $$  \ $$  | $$  | $$  \__/   | $$  | $$  \ $$| $$$$| $$| $$  \__/| $$      
| $$      |  $$$$$$ | $$$$$$$$      | $$  | $$  | $$  |  $$$$$$    | $$  | $$$$$$$$| $$ $$ $$| $$      | $$$$$   
| $$       \____  $$| $$__  $$      | $$  | $$  | $$   \____  $$   | $$  | $$__  $$| $$  $$$$| $$      | $$__/   
| $$       /$$  \ $$| $$  | $$      | $$  | $$  | $$   /$$  \ $$   | $$  | $$  | $$| $$\  $$$| $$    $$| $$      
| $$$$$$$$|  $$$$$$/| $$  | $$      | $$$$$$$/ /$$$$$$|  $$$$$$/   | $$  | $$  | $$| $$ \  $$|  $$$$$$/| $$$$$$$$
|________/ \______/ |__/  |__/      |_______/ |______/ \______/    |__/  |__/  |__/|__/  \__/ \______/ |________/
"""

LSVF_TEXT = """
 /$$        /$$$$$$  /$$    /$$ /$$$$$$$$
| $$       /$$__  $$| $$   | $$| $$_____/
| $$      | $$  \__/| $$   | $$| $$      
| $$      |  $$$$$$ |  $$ / $$/| $$$$$   
| $$       \____  $$ \  $$ $$/ | $$__/   
| $$       /$$  \ $$  \  $$$/  | $$      
| $$$$$$$$|  $$$$$$/   \  $/   | $$      
|________/ \______/     \_/    |__/      
"""