// 1. 变量命名
// 2. 变量赋值方法
package main

import "fmt"

func main() {
	// 有效的标识符必须以字母（可以使用任何 UTF-8 编码的字符或 _）开头，然后紧跟着 0 个或多个字符或 Unicode 数字
	// 命名要求：
	// 1. 不能使用如下 25 个保留字（语法错误）
	//   break	default	func	interface	select
	//   case	defer	go	map	struct
	//   chan	else	goto	package	switch
	//   const	fallthrough	if	range	type
	//   continue	for	import	return	var
	// 2. 不能以数字开头
	// 3. 不能包含运算符，比如+-*/&%等
	// 4. 不要使用如下36个预定义标识符（虽然不会有语法错误）
	//    append	bool	byte	cap	close	complex	complex64	complex128	uint16
	//    copy	false	float32	float64	imag	int	int8	int16	uint32
	//    int32	int64	iota	len	make	new	nil	panic	uint64
	//    print	println	real	recover	string	true	uint	uint8	uintptr

	// 两种定义变量的方法
	var yourName string = "小芳" // 建议的命名方法(英文驼峰)
	yourAge := 18              // 建议的命名方法(英文驼峰)

	// 空白标识符 _
	//  它可以像其他标识符那样用于变量的声明或赋值（任何类型都可以赋值给它）
	//  任何赋给这个标识符的值都将被抛弃
	//  这些值不能在后续的代码中使用，也不可以使用这个标识符作为变量对其它变量进行赋值或运算。

	fmt.Println(yourName, "is", yourAge, "years old.")
}
