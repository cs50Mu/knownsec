### 批量重命名
`for i in *.txt; do mv $i "${i/.txt/}.jpg"; done`
用到的知识是变量替换
	举例
	foo=JPG.JPG
	echo ${foo/JPG/jpg}  ===》  jpg.JPG
	echo ${foo//JPG/jpg} ===》 jpg.jpg  #全局替换
还有其它一些字符串操作：

There is a large set of expansions that can be used to operate on strings. Many of these
expansions are particularly well suited for operations on pathnames.
${#parameter}   expands into the length of the string contained by parameter.
	举例
	[me@linuxbox ~]$ foo="This string is long."
	[me@linuxbox ~]$ echo "'$foo' is ${#foo} characters long."
	'This string is long.' is 20 characters long.

${parameter:offset}
${parameter:offset:length}
These expansions are used to extract a portion of the string contained in parameter. The
extraction begins at offset characters from the beginning of the string and continues until
the end of the string, unless the length is specified.
	举例
	[me@linuxbox ~]$ foo="This string is long."
	[me@linuxbox ~]$ echo ${foo:5}
	string is long.

${parameter#pattern}
${parameter##pattern}
These expansions remove a leading portion of the string contained in parameter defined
by pattern. pattern is a wildcard pattern like those used in pathname expansion. The dif-
ference in the two forms is that the # form removes the shortest match, while the ## form
removes the longest match.
	举例
	[me@linuxbox ~]$ foo=file.txt.zip
	[me@linuxbox ~]$ echo ${foo#*.}
	txt.zip
	[me@linuxbox ~]$ echo ${foo##*.}
	zip

${parameter%pattern}
${parameter%%pattern}
These expansions are the same as the # and ## expansions above, except they remove
text from the end of the string contained in parameter rather than from the beginning.
	举例
	[me@linuxbox ~]$ foo=file.txt.zip
	[me@linuxbox ~]$ echo ${foo%.*}
	file.txt
### 取出/etc/passwd文件中shell出现的次数
`cat /etc/passwd|awk -F: '{print $7}'|sort|uniq -c`

-F:用于指定段分隔符为冒号，uniq的-c选项指示统计个数
### 打印本机交换分区大小
`top -n 1|grep Swap|awk '{print $2,$3/1024"M"}'`
### 打印文件的第一行
`sed -n '1p' filename`
注意，一定要有-n选项，否则会全部打印出来
### 在目录/tmp下找到100个以abc开头的文件，然后把这些文件的第一行保存到文件new中
#!/bin/bash
	for f in `find /tmp -type f -name "abc*"|head -n 100`
	do
	sed -n '1p' $f >> new
	done
### 把文件b中有的，但a文件中没有的所有行，保存为文件c，并统计c的行数
`grep -vxFf a b|tee c|wc -l`
-v表示不选择匹配的行，-f a 表示匹配模式来自文件a
### 小技巧
- `ALT+.` or `<ESC> + .`  把上次命令行的参数调出来
- `!$`代表上一个命令的最后一个字符串。应用场景     
	mkdir mydir
	mv !$ yourdir

