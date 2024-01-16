import streamlit as st
import pandas as pd
import numpy as np
import torch
st.title("Welcome to Streamlit")
t = torch.rand(2,3,3)
st.write(t)
