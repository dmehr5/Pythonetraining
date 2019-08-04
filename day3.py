{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "harry\n",
      "dumbeldore\n",
      "hormanie\n",
      "anand\n"
     ]
    }
   ],
   "source": [
    "#Introduction to loops\n",
    "#looping through an entire list #iteration\n",
    "\n",
    "magicians = ['harry','dumbeldore','hormanie','anand']\n",
    "\n",
    "for magician in magicians:\n",
    "    print(magician)\n",
    "    \n",
    "    #space is called indentation. 4 lines of free space advised by the zen pf python \n",
    "    #magician - creation of a temp variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Harry,that was a great trick!\n",
      "Dumbeldore,that was a great trick!\n",
      "Hormanie,that was a great trick!\n",
      "Anand,that was a great trick!\n"
     ]
    }
   ],
   "source": [
    "magicians = ['harry','dumbeldore','hormanie','anand']\n",
    "\n",
    "for x in magicians:\n",
    "    print(f\"{x.title()},that was a great trick!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I cannot wait to see your next trick,Harry\n",
      "I cannot wait to see your next trick,Dumbeldore\n",
      "I cannot wait to see your next trick,Hormanie\n",
      "I cannot wait to see your next trick,Anand\n"
     ]
    }
   ],
   "source": [
    "magicians = ['harry','dumbeldore','hormanie','anand']\n",
    "\n",
    "for n in magicians:\n",
    "    print(f\"I cannot wait to see your next trick,{n.title()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I cannot wait to see your next trick,Harry\n",
      "I cannot wait to see your next trick,Dumbeldore\n",
      "I cannot wait to see your next trick,Hormanie\n",
      "I cannot wait to see your next trick,Anand\n",
      "I cannot wait to see your next trick,Anand\n"
     ]
    }
   ],
   "source": [
    "magicians = ['harry','dumbeldore','hormanie','anand']\n",
    "\n",
    "for n in magicians:\n",
    " print(f\"I cannot wait to see your next trick,{n.title()}\")\n",
    "    \n",
    "print(f\"I cannot wait to see your next trick,{n.title()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n",
      "11\n",
      "12\n",
      "13\n",
      "14\n",
      "15\n",
      "16\n",
      "17\n",
      "18\n",
      "19\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "#making for numerical list....!!\n",
    "for x in range(1,21):\n",
    "    print(x)\n",
    "    \n",
    "#how to the range function works\n",
    "\n",
    "#non inclusive and exclusive value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "#using range fuction to make a list of numbers\n",
    "numbers=list(range(1,6))\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\n",
      "[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\n"
     ]
    }
   ],
   "source": [
    "#printing the even numbers in the given range.\n",
    "\n",
    "even_numbers=list(range(2,21,2))\n",
    "print(even_numbers)\n",
    "\n",
    "odd_numbers=list(range(1,21,2))\n",
    "print(odd_numbers)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#how to perform a simple statistical operations on a list.\n",
    "\n",
    "digits=[1,2,3,4,5,6,9]\n",
    "\n",
    "min(digits)\n",
    "\n",
    "max(digits)\n",
    "\n",
    "sum(digits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['dhoni', 'dravid', 'kumble']\n",
      "['saching', 'dhoni', 'dravid', 'kumble']\n"
     ]
    }
   ],
   "source": [
    "#slicing of a list...**\n",
    "\n",
    "players=['yuvraj','saching','dhoni','dravid','kumble']\n",
    "\n",
    "#I want to print out only the values from dhoni to kumble...\n",
    "\n",
    "print(players[2:5])\n",
    "\n",
    "print(players[1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
