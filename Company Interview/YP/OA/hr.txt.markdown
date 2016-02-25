1. Linux中grep是什么意思
2. What is the command to check if a host is online?(ping+IP地址).
3. 网页传输用什么协议(TCP/IP)
4. HTML默认端口号是多少(我回答的是80或者443，应该是80)
5. 64bit的机器是几个byte(8个)
6. SQL里面，删除一行用什么指令(delete)
7. Linkedlist和arraylist的区别(这个简单，CS常识).
8. sorted array的binary search复杂度(log n)
9. sql的inner join是交并差？
10. ip和域名的映射是怎么样完成的(DNS, domain name system)
11. 举例说明deadlock。我就说了下CC上面那个拿筷子和放筷子的例子，又说了下不同thread访问一个文件。后来引申问有什么么检测的方法。我說了可以 timeout 和用其他的service建graph遍历来检测，后来又问了为什么dfs比bfs检测graph的环好。

12. 中间问了些基础知识，比如像C++ vector list等等数据结构查找删除 size()的时间复杂度.
13. c++和java区别 （本人主要语言C++）
14. java GC 工作机制
15. post get区别 怎么保证post请求不被中间人篡改
16. 数据库index什么原理，B树和hash table优缺点: B tree 的search time 是logN, 但是好處是range search的時候快。Hash table的edit, search time都是O(1), 缺點是range search的時候非常慢
17. HTTP: GET vs POST. Why POST is not cachable..（http://stackoverflow.com/questions/626057/is-it-possible-to-cache-post-methods-in-http）
18. Java: pass by reference or pass by value? what does pass by value mean?
19. Database: Left join and Inner Join.
如果一个Database的查询速度很慢，如何改进。如果denormalization之后还是不给力，怎么办？
20. How many bits does one need to represent a single octal digit? 3
21. Biggest unsigned integer in Java?. （there is no unsigned int in java ）
22.What is the time complexity to insert an element at head of a linked list?
23. SSL stands for?
24. How to map ip to server?
25. What is the result of inner join? intersection, union, or difference?
26. What is your HTTP port number? What is the Protocol?
27. What is the linux command line for searching a method in a source code?

*****************
General Questions
*****************
1. unix里面 Kill 的信号量是哪个数字。  我答: 9
2. 在很多源代码文件中查找一个特定的函数用什么命令。 我答: grep 
3. SQL里面删除行记录使用什么命令。 我答： DELETE
4. 用什么命令看一个主机是否在线。  我答：ping
5. HTTP端口号是多少，用什么协议。 我答：80, TCP

binary search複雜度 1byte = __ bits 之類的 HTTP port number =?
http port number啦difference between process&thread之类

64bit的integer里有多少个byte
octal的byte里有几个bit
java unsigned int最大能表示多少
binary search的时间复杂度. From 1point 3acres bbs
binary search应该用sorted array还是linked list
linked list头上插入一个元素，worst case时间复杂度
SSL的全称

64bit的integer里有多少个byte 8
octal的byte里有几个bit 3
DNS.. MAP to IP
java unsigned int最大能表示多少 2^32-1
binary search的时间复杂度 log(n)
binary search应该用sorted array还是linked list sorted list
linked list头上插入一个元素，worst case时间复杂度
SSL的全称 secured scokets layer

1. 怎么样提高数据库的搜索效率？. 1point3acres.com/bbs
2. 是不是越多index, 数据库效率越高？
3. Java的garbage collector: 如果有两个object互相reference, 这两个object会不会回收？怎么回收？

之后是十几道问答题，题目的内容和网上给的差不多，基本都是网络，数据库，操作系统一类的内容。比如HTTP，SSL，DNS等等。

   * what comman to use to  find all instances of method in source code 
   * how many bits in a single octal digit
   * remove a row from sql
    *maximum value of 32 unsigned digt
    
************* 
Code Question
*************
1.  sort id
==========
我的朋友碰到的一道题，在stadin里输入一些id，value的pair， 让你根据value排序。这里注意输入的pair可以是任意个。需要用到一个while循环

---

第二部分 20分钟 一道coding题。
输入数据是这样的。一行一组数据，由空格分开两个数，分别是 ID 和 rating， ID不会重复，最多10000.
ID1  Rating1.
ID2  Rating2.
ID3  Rating3
...
IDn  Ratingn.
. 1point3acres.com/bbs
让你根据Rating从大到小排序，再输出。
比如 输入 是
103  1
104  2
105  3
输出就是
105 3
104 2
103 1

题目很简单。但是需要自己处理 STDIN 和 STDOUT。
自己花了好多时间去google怎么用java处理 STDIN。。。上次用java处理STDIN貌似是3年前的事了。。。
导致后面没时间了直接赶紧写了一个O(n^2)的冒泡排序。。
真心吃了一次亏。。。

================
2. anagram check
================

第二部分 20分钟的编程 anagram check， 看两个string是不是anagram.
输入stdin不太懂，输出stdout应该就是System.out.println
所以程序写了没有跑出来

---

Coding problem:
1. leetcode anagram
2. Follow up: 怎么用map reduce做？

=================
3.  palidrom check
=================

Code test:
palidrom test

if can be turned into palindrome return 'true' example 'aab'->'true'
'abc'->'false'
otherwise 'false'
Bless!!!

---

check palindrom : if  yes, return true; if no, return false .
public class{
public static void main(String [] args) {
// read from std input;
}
}

这个function本事是毫无难度。但是我到现在都没弄明白的是,这个题目是希望
我们把这个function 写在main methon 里面嘛？然后这个online judge 到底是
怎么test 的？ 是给一个input.txt 和一个output.txt.然后要read from input.txt;
再write to output.txt? 

我自己是单独在solution class写了一个 checkPalindrom class, 再在main metho里面
加了一个file reader 和write ,一边read from file,一边call checkPalindrom 这个function
很明显不对。。

用BufferedReader去读System.in,然后输出就是System.out.println啥的，hackerrank很多题目都是在main里面写的。
http://www.mkyong.com/java/how-to-get-the-standard-input-in-java/

==============
4.  dot product
==============

编程题就是给两个sparse vector,然后求dot product.

================
5.  reverse words
================

我的题目是把一个句子按单词reverse，连标点符号都没有。所以用python的话，几乎一行代码可以搞定。

