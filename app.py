import gradio as gr

def linear_search(arr_str, target):
    try:
        if not arr_str.strip() or not target.strip():
            return "Input cannot be empty. Please enter an array and a target value."

        try:
            arr = [int(x.strip()) for x in arr_str.split(",") if x.strip()]
        except ValueError:
            return "Input must be integers separated by "","" e.g., 1,3,5,7,9"

        try:
            target = int(target)
        except ValueError:
            return "Target value must be an integer, e.g., 5"

        if len(arr) == 0:
            return "Input cannot be empty. Please enter at least one integer."

        steps = []
        for i, val in enumerate(arr):
            steps.append(f"Step {i+1}: Compare {val} with {target}")
            if val == target:
                steps.append(f"Found {target} at index {i}")
                steps.append(f"Total comparisons: {i+1}")
                return "\n".join(steps)
        steps.append("Target not found")
        steps.append(f"Total comparisons: {len(arr)}")
        return "\n".join(steps)

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

demo = gr.Interface(
    fn=linear_search,
    inputs=[
        gr.Textbox(
            label="Enter array",
            placeholder="Example: 1,3,5,7,9"
        ),
        gr.Textbox(
            label="Enter target value",
            placeholder="Example: 5"
        )
    ],
    outputs = gr.Textbox(label="Result", lines=12),
    title="Linear Search Visualizer"
)

demo.launch()
