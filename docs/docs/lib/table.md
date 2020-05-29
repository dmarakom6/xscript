# table - 字符型表格

光在debug中用`prettytable`模块就太浪费了.

*addColum &table $fieldname column...*
  
  - *table* - 一个表格对象
  - *fieldname* - 列名
  - *colum* - 列数据

> 在表格中添加一列

- - -

*addRow &table row...*

  - *table* - 一个表格对象
  - *row* - 行数据

> 在表格中添加一行数据

- - -

*clear &table*

  - *table* - 表格对象
> 删除整张表格

- - -

*clearRow &table*

  - *table* - 一个表格对象

> 删除表格中所有的行, 但保留标题.

- - -

*delRow &table \#row_index*

  - *table* - 一个表格对象
  - *row_index* - 要删除的行(从0开始)

> 从表格中删除一行

- - -

*Table $field_names...*

  - *field_names* - 列名

> 创建一个表格
