import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [task, setTask] = useState('');
  const [taskList, setTaskList] = useState([]);

  const addTask = event => {
    setTask(event.target.value);
  }
  const displayTasks = () => {
    const aTask = {
      taskName: task,
      id: taskList.length === 0 ? 1 : taskList[taskList.length - 1].id + 1,
      completed: false,
    }
    setTaskList([...taskList, aTask]);
    console.log(aTask);
  }
  const deleteTask = id => {
    setTaskList(taskList.filter(task => task.id !== id));
  }
  const completeTask = id => {
    setTaskList(taskList.map(task => {
      if (task.id === id) {
        return {...task, completed:true}
      } else {
        return task;
      }
    }))
  }
  
  // useEffect(() => {},[])
  return (
    <>
      <div>
        <input type="text" name="task" placeholder='Add task here...'  onChange={addTask} className='input-div'/>
        <button type="submit" id='btn' onClick={displayTasks}>Add Task</button>
      </div>
      <div className='tasks-div'>
        {taskList.map(task => {
          return <div key={task.id}
            className='atask-div' style={{backgroundColor: task.completed ? 'green' : 'maroon'}}>
            <h2>{task.taskName}</h2>
            <div className='btn-div'>
              <button onClick={() => completeTask(task.id)}>completed</button>
              <button onClick ={() => deleteTask(task.id)}>delete</button>
            </div>
          </div>
        })}
      </div>
    </>
  )
}

export default App;
