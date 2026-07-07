import streamlit as st

st.set_page_config(page_title="Smart To-Do App", page_icon="✅")


def initialize_tasks():
    if "tasks" not in st.session_state:
        st.session_state.tasks = []


def add_task(task_text):
    if task_text.strip():
        st.session_state.tasks.append({
            "task": task_text,
            "completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task before adding.")


def get_filtered_tasks(filter_option):
    filtered = []
    for index, task in enumerate(st.session_state.tasks):
        if filter_option == "All":
            filtered.append((index, task))
        elif filter_option == "Completed" and task["completed"]:
            filtered.append((index, task))
        elif filter_option == "Pending" and not task["completed"]:
            filtered.append((index, task))
    return filtered


def display_tasks(tasks_to_show):
    if not tasks_to_show:
        st.info("No matching tasks found.")
        return

    for index, item in tasks_to_show:
        col1, col2, col3 = st.columns([6, 2, 2])

        with col1:
            completed = st.checkbox(
                item["task"],
                value=item["completed"],
                key=f"task_{index}"
            )
            st.session_state.tasks[index]["completed"] = completed

        with col2:
            st.write("Done" if item["completed"] else "Pending")

        with col3:
            if st.button("Delete", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()


def main():
    st.title("✅ Smart To-Do App")
    st.write("A simple to-do app built with Streamlit.")

    initialize_tasks()

    new_task = st.text_input("Enter a new task")

    if st.button("Add Task"):
        add_task(new_task)

    st.divider()

    filter_option = st.selectbox(
        "Filter tasks",
        ["All", "Completed", "Pending"]
    )

    st.subheader("Your Tasks")
    filtered_tasks = get_filtered_tasks(filter_option)
    display_tasks(filtered_tasks)


if __name__ == "__main__":
    main()