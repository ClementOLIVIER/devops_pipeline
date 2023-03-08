import streamlit as st
from io import StringIO
from contextlib import contextmanager, redirect_stdout

# Print redirection
@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write

        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret

        stdout.write = new_write
        yield


def function_runner(function_to_run, *args):
    output = st.empty()
    with st.spinner(text="Running the function..."):
        with st_capture(output.code):
            function_to_run(*args)
        st.success('Function ran successfully')
        st.balloons()
