# Đệ quy
## Định nghĩa
- Cách định nghĩa được gọi là định nghĩa kiểu đệ quy nếu trong định nghĩa đó có sử dụng chính khái niệm đó, ví dụ:
    - Số 0 là một số nguyên không âm
    - Số n khác 0 là một số nguyên không âm nếu n - 1 là một số nguyên không âm

    hay:
    
    - 0! = 1
    - n! = (n - 1)! * n với n != 0

- Đệ quy cũng là một quy chuẩn cú pháp của các ngôn ngữ lập trình bậc cao, cho phép gọi một hàm ngay trong hàm đó (định nghĩa hàm này bằng chính hàm đó)

## Bài toán đệ quy:
Bài toán đệ quy

## Ví dụ về hàm đệ quy:
Sử dụng định nghĩa vừa rồi của giai thừa, ta có thể lập trình hàm viết phép tính giai thừa như sau:
```python
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
```
Làm bài [factorial](./factorial/factorial.md) 


## Base case:
Mọi định nghĩa kiểu đệ quy cần một trường hợp gốc, qua đó các định nghĩa khác được xây dựng:

Ví dụ:
- Số 0 là một số nguyên không âm (trường hợp gốc)
- Số n khác 0 là một số nguyên không âm nếu n - 1 là một số nguyên không âm

hay:

- 0! = 1 (trường hợp gốc)
- n! = (n - 1)! * n với n != 0

Khi viết các bài toán đệ quy, cần xác định chính xác trường hợp gốc, phải đảm bảo được bài toán đệ quy có thể đạt đến trường hợp gốc, nếu không hàm đệ quy sẽ bị lặp vô tận.
Làm bài [fibonacci](./fibonacci/fibonacci.md)
Ví dụ:
```python
def fibonacci(n):
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Đoạn code này sẽ rơi vào vòng lặp vô hạn, nếu hàm này được truyền vào giá trị n là 1. Khi đó, hàm sẽ tính giá trị `fibonacci(1) = fibonacci(0) + fibonacci(-1)`. Giá trị `fibonacci(-1)` này sẽ được tính bằng `fibonacci(-2) + fibonacci(-3)` và cứ thế lặp lại mãi.

Cách giải quyết: Đặt thêm một base case với n == 1. Khi đó, `fibonacci(2) = fibonacci(1) + fibonacci(0)` và đây là hai base case đã được định sẵn, quá trình đệ quy dừng lại tại đây.

## Bài tập:
- [Tính ước chung nhỏ nhất](./gcd/gcd.md)
- [Tìm giá trị nhỏ nhất trong một list](./min/min.md)
- [Tính phép luỹ thừa bằng đệ quy](./power)
