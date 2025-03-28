import marimo

#__generated_with = "0.10.9"
app = marimo.App(width="medium")

'''
@app.cell
def _():
    #import numpy as np
    #import altair as alt
    #import pandas as pd
    #import marimo as mo
    #return alt, mo, np, pd
'''

@app.cell
def _(mo):
    mo.md(
        """
        # Hello World

        This notebook demonstrates a simple hello world in marimo app mode.
        """
    )
    return

'''
@app.cell
def _(alt, mo, np, pd):
    # Create sample data
    data = pd.DataFrame({"x": np.arange(100), "y": np.random.normal(0, 1, 100)})

    # Create interactive chart
    chart = mo.ui.altair_chart(
        (
            alt.Chart(data)
            .mark_circle()
            .encode(x="x", y="y", size=alt.value(100), color=alt.value("steelblue"))
            .properties(height=400, title="Interactive Scatter Plot")
        )
    )
    chart
    return chart, data


@app.cell
def _(chart):
    chart.value
    return
'''

if __name__ == "__main__":
    app.run()
