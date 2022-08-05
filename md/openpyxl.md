# Font 字体设置

| 序号 |   参数    |      含义      |              样例              |
| :--: | :-------: | :------------: | :----------------------------: |
|  1   |   name    |    字体名称    |           '微软雅黑'           |
|  2   |   size    |    字体大小    |              '14'              |
|  3   |   bold    |    是否加粗    |           True/False           |
|  4   |  italic   |    是否斜体    |           True/False           |
|  5   |   color   |    字体颜色    |            'FF0000'            |
|  6   |  strike   |     删除线     |           True/False           |
|  7   | vertAlign | 上标/下标/基线 | superscript/subscript/baseline |
|  8   | underline |     下划线     |         single/double/         |



# Alignment 对齐设置

| 序号 | 参数          | 含义         | 样例                                                         |
| ---- | ------------- | ------------ | ------------------------------------------------------------ |
| 1    | horizontal    | 水平对齐     | 左对齐left，居中center，右对齐right，分散对齐distributed，跨列居中centerContinuous，两端对齐justify，填充fill，常规general |
| 2    | vertical      | 垂直对齐     | 居中center，靠上top，靠下bottom，两端对齐justify，分散对齐distributed |
| 3    | text_rotation | 文字旋转角度 | 45                                                           |
| 4    | wrap_text     | 是否自动换行 | True/False                                                   |
| 5    | shrink_to_fit | 自动缩放     |                                                              |
| 6    | indent        | 缩进         |                                                              |



# Side 边框样式

| 序号 | 参数   | 含义     | 样例                                                         |
| ---- | ------ | -------- | ------------------------------------------------------------ |
| 1    | style  | 边线样式 | 'double, 'mediumDashDotDot', 'slantDashDot',  'dashDotDot','dotted','hair', 'mediumDashed, 'dashed', 'dashDot', 'thin',  'mediumDashDot','medium', 'thick' |
| 2    | color  | 边线颜色 | 'FF0000'                                                     |
| 3    | Border |          | left=左边线样式，right=右边线样式，top=上边线样式，bottom=下边线样式 |
|      |        |          |                                                              |
|      |        |          |                                                              |



### PatternFill 、GradientFill填充样式

| 序号         | 参数      | 含义     | 样例                              |
| ------------ | --------- | -------- | --------------------------------- |
| PatternFill  | fill_type | 填充样式 | "solid"                           |
|              | fgColor   | 填充颜色 | "99ccff"                          |
|              |           |          |                                   |
| GradientFill | stop      | 渐变颜色 | stop=("FFFFFF","99ccff","000000") |
|              |           |          |                                   |

