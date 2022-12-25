import streamlit as st
import pandas as pd

st.title('Startup Dashboard')
st.subheader('And I am loving it!')
st.write('This is a normal text.')
st.markdown("""
### My favorite movies
- Race 2
- Humsakals
- Gunday
""")
st.code(""""
def foo(input):
    return foo*2

x=foo(2)    
""")

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'name': ['amit', 'ankit', 'deepak'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')

st.json(
    {
        'name': ['amit', 'ankit', 'deepak'],
        'marks': [50, 60, 70],
        'package': [10, 12, 14]
    }
)

st.image('data.jpg')
# st.video('01.mp4')

st.sidebar.title('sidebar')

col1, col2 = st.columns(2)

with col1:
    st.image('data.jpg')

with col2:
    st.image('data.jpg')

st.error('login failed')
st.success('login successful')

