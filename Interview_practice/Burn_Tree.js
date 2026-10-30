// # Problem statement
// # You have a binary tree of 'N' unique nodes and a Start node from where the tree will start to burn. Given that the Start node will always exist in the tree, your task is to print the time (in minutes) that it will take to burn the whole tree.



// # It is given that it takes 1 minute for the fire to travel from the burning node to its adjacent node and burn down the adjacent node.



// # For Example :
// # For the given binary tree: [1, 2, 3, -1, -1, 4, 5, -1, -1, -1, -1]
// # Start Node: 3

// #     1
// #    / \
// #   2   3
// #      / \
// #     4   5

// # Output: 2

// # Explanation :
// # In the zeroth minute, Node 3 will start to burn.

// # After one minute, Nodes (1, 4, 5) that are adjacent to 3 will burn completely.

// # After two minutes, the only remaining Node 2 will be burnt and there will be no nodes remaining in the binary tree. 

// # So, the whole tree will burn in 2 minutes.
// # Detailed explanation ( Input/output format, Notes, Images )
// # Sample Input 1 :
// # 1 2 3 4 -1 -1 5 -1 -1 -1 -1
// # 2    
// # Sample Output 1 :
// # 3
// # Explanation Of Sample Input 1 :
// # The given binary tree will look as - 

// # The Start node is 2.

// # In the zeroth minute, Node 2 will start to burn.

// # After one minute, Nodes 1 and 4 that are adjacent to 2 will burn completely.

// # After two minutes, Node 3 that is adjacent to node 1 will burn completely.

// # After three minutes, the only remaining Node 5 will be burnt and there will be no nodes remaining in the binary tree i.e the whole tree will burn in 3 minutes.
// # Sample Input 2 :
// # 3 1 2 5 6 -1 -1 -1 -1 -1 -1
// # 3
// # Sample Output 2 :
// # 2
// # Constraints :
// # 1 <= N <= 10^5
// # 1 <= Value of Tree Node <= 10^9
// # 1 <= Value of Start Node <= 10^9

// # Time limit: 1 sec
// # Javascript (node v10.20.0)
// # 34567891011121314151617181920212223242526272829303132

// # /* Declare and implement your function here 
// # eg: function example(parameter_name1,parameter_name2....){}
// # Handle the input/output from main()
// # */




// # process.stdin.resume();


function timeToBurnTree(root, start) {
    if (!root) return 0;

    // PHASE 1: Build parent mapping and find start node

    const parentMap = new Map();
    const queue = [root];
    let front = 0;
    let startNode = null;

    while (front < queue.length) {
        const node = queue[front++];

        if (node.data === start) {
            startNode = node;
        }

        if (node.left) {
            parentMap.set(node.left, node);
            queue.push(node.left);
        }

        if (node.right) {
            parentMap.set(node.right, node);
            queue.push(node.right);
        }
    }

    // PHASE 2: Spread fire using BFS

    const visited = new Set();
    const fireQueue = [startNode];

    visited.add(startNode);

    let minutes = 0;
    let fireFront = 0;

    while (fireFront < fireQueue.length) {

        const levelSize = fireQueue.length - fireFront;
        let spread = false;

        for (let i = 0; i < levelSize; i++) {

            const node = fireQueue[fireFront++];

            const neighbors = [
                node.left,
                node.right,
                parentMap.get(node)
            ];

            for (const neighbor of neighbors) {

                if (neighbor && !visited.has(neighbor)) {

                    visited.add(neighbor);
                    fireQueue.push(neighbor);

                    spread = true;
                }
            }
        }

        if (spread) {
            minutes++;
        }
    }

    return minutes;
}
