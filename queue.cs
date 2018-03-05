// Programmed by MD. Mehedi Hasan

using System;
using System.Collections;

namespace QueueAPP {

    class Queue_Operations {
        
        static void Main(string[] args) {
            
            Queue q = new Queue();    // create and initialize a new queue
            q.Enqueue('A');
            q.Enqueue('B');
            q.Enqueue('C');
            q.Enqueue('D');
         
            Console.Write("Current queue: ");
            PrintValues(q);    // printing the queue

            Console.WriteLine();

            // adding new element to the queue
            q.Enqueue('E');
            q.Enqueue('F');
            
            Console.Write("Current queue after enqueue operation: ");
            PrintValues(q);    // printing the queue

            Console.WriteLine("\n");

            Console.WriteLine("Removing values by dequeue operation ...");
            Console.Write("Removed values: {0}, {1}", q.Dequeue(), q.Dequeue());    // removing element from the queue

            Console.WriteLine("\n");

            Console.Write("Current queue after dequeue operation: ");
            PrintValues(q);    // printing the queue

            Console.ReadKey();
        }

        // this function print queue element's 
        public static void PrintValues (IEnumerable myCollection) {

            foreach (object obj in myCollection) {

                Console.Write(obj + " ");
            }
        }
    }
}