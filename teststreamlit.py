import streamlit as st

# 1. For creating grids
#==========================================================================
from streamlit_extras.grid import grid
import numpy as np
import pandas as pd

def example():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)

example()

#==========================================================================
# 2. For creating simple columns
#==========================================================================
# col1, col2, col3 = st.columns([1, 1, 1])
# with col1:
#     st.write("Column 1")
#     st.write("Content A")

# # Adding elements to the second column
# with col2:
#     st.write("Column 2")
#     st.write("Content B")

# # Adding elements to the third column
# with col3:
#     st.write("Column 3")
#     st.write("Content C")

#==========================================================================
