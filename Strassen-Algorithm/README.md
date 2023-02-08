# Strassen Algorithm

- To make this code run, you need to install numpy in your computer
- To the input that the program asks, you should introduce the path of the csv matrix

### Authors

- Diego Araque - A01026037
- Uriel Martinez - A01781698
- Luis Fernando - A01745186
- Marco Antonio - A01025334

## Explanation of the strassen algorithm we implemented:

- Strassen is an algorthm for the multiplication of two order 𝑛 matrixes 𝐴,𝐵 ∈ 𝕄!(ℝ)

Strassen's algorithm uses seven elementary operations to multiply two matrix of order 2.

$$
\begin{array}{l}
M_{1}=\left(A_{11}+A_{22}\right)\left(B_{11}+B_{22}\right) \\
M_{2}=\left(A_{21}+A_{22}\right) B_{11} \\
M_{3}=A_{11}\left(B_{12}-B_{22}\right) \\
M_{4}=A_{22}\left(B_{21}-B_{11}\right) \\
M_{5}=\left(A_{11}+A_{12}\right) B_{22} \\
M_{6}=\left(A_{21}-A_{11}\right)\left(B_{11}+B_{12}\right) \\
M_{7}=\left(A_{12}-A_{22}\right)\left(B_{21}+B_{22}\right)
\end{array}
$$

The result matrix is going to be:

$$
\begin{array}{l}
C_{11}=M_{1}+M_{4}-M_{5}+M_{7} \\
C_{12}=M_{3}+M_{5} \\
C_{21}=M_{2}+M_{4} \\
C_{22}=M_{1}-M_{2}+M_{3}+M_{6}
\end{array}
$$

$$
\left[\begin{matrix}c_{11}&c_{12}\\
c_{21}&c_{22}\end{matrix}\right]
$$

If the matrix given to the program is bigger than order 2, the program will <code>call divide_half()</code>, it divides the matrix in four submatrixes and runs again all the operations for each pair of matrix, at the end an stack of operations for each multiplication of matrixes bigger than order 2 will be created.

Notice that when we call <code>multiply(A, B)</code>, we are calling everything recursively. Which makes us leave operations on stand by, until we reach the scalar multiplications. You may think that we are still doing more operations, but that is not completely true. With this formulas, we perform 7 multiplications per level, as for a brute force algorithm we will perform 8. We do make more sum operations, but it'a easier for a machine to compute this than a multiplication.

Making this process we can multiply two matrix with temporaly complex of:

$$ n^{\log \_{2} 7}+O\left(n^{2}\right) $$

### Results

To analyse our results, we compared the textbook solution with strassen's algorithm on a matrix of order of 128.

- Strassen algorithm

<img width="614" alt="Screen Shot 2022-09-02 at 1 12 08 AM" src="https://user-images.githubusercontent.com/84464594/188070529-b60d60ef-80cb-47ec-99b6-7e8fcfc9bae8.png">
Since it is a matrix of order 128, we know the amount of scalar multiplications it will take. By substituting n with 128

$$ 128^{\log \_{2} 7}=823543$$

This is the same result, we got from our program. Which proves that it is being implemented well.

To offer some contrast, we present the result of the textbook algorithm (brute force).

- Textbook algorithm

We know that multiplyng matrixes by brute force has the followin time complexity:

$$ O(n^3) $$

<img width="584" alt="Screen Shot 2022-09-02 at 1 12 28 AM" src="https://user-images.githubusercontent.com/84464594/188070569-63277ab1-c4e8-4d7b-b38b-c8cb433980de.png">

This same formula helps us get the value of scalar multiplications we perform, which will be the following:

$$ 128^3=2097152 $$

We notice that the difference is significant, the textbook algorithm reaches almost 2 million scalar multiplications, while strassen's algorithm performs less than half.

### Conclusion

In our opinion, for big matrixes strassen's algorithm is the way to go, but for small matrixes (order 2, 4, 8) we believe we should stick with the brute force algorithm. Mainly because the difference wouldn't be noticable, and considering it is a very complex algorithm it may not be worth it to spend a lot of time on the implementation.
