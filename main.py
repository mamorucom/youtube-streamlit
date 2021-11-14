import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFreme')

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# 表の細かい設定はできない
# st.write(df)

# 表の細かい設定ができる
# st.dataframe(df.style.highlight_max(axis=0), width=600, height=600)

# staticなテーブル
# st.table(df.style.highlight_max(axis=0))

# # マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

# 折れ線グラフ
st.line_chart(df)
# エリアチャート
st.area_chart(df)
# 棒グラフ
st.bar_chart(df)