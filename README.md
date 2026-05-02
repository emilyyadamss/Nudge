# Nudge
This project is a personal productivity tool that is designed to help users manage multiple small goals by intelligently distributing time across them. The core problem it solves is decision fatigue. When you have many goals, it becomes difficult to decide what to work on. The app removes that friction by algorithmically selecting which goal deserves your attention each day.

## For Project Setup
In pulling the project, make sure python(3) and pip are installed in the IDE. Then create a virtual environment with 
```jsx
python3 -m venv venv
```
Activate it by, 
```jsx
source venv/bin/activate
```
to deactivate, simply type 'deactivate'. 

Install in the virtual environment, 
```jsx 
pip install fastapi uvicorn 
```
Then install Vite and React 
```jsx 
npm create vite@latest 
``` 
With React and regular Javascript. 

### Backend Start
CD into the backend directory and activate the virtual environment. Then run this command: 
```jsx
uvicorn app.main:app --reload  
```

### Frontend Start
CD into the frontend directory and it would automatically activate the virtual environment. Then run this command: 
```jsx 
npm run dev 
```

## Purpose and Problem Statement
Users with many small goals often face two challenges: 
- Difficulty deciding what to work on each day, leading to inactivity.
- Unconsciously spending most time on comfortable or interesting goals while neglecting others.
  
The goal is that both problems are solved by using a weighted random algorithm to surface neglected goals more frequently, ensuring that there is a balance between the users goals over time.

## Algorithm, How it Works

 The user enters in a goal, assign it to a category,  set a date which they wish to complete it, how much of a priority it is, etc. As of right now, each category is weighed differently (i.e. languages, coding, gardening), where if its more of a task, it would be based on one completed task per day, or 30 minutes per day, etc. 

The current formula is: 

```jsx
weight = 10 / ( 1 + hours logged ) 
```

Meaning, a goal with zero hours logged is x10 more likely to be picked than a goal with 10 hours logged. The algorithm does not completely exclude well-worked goals, it simply deprioritizes them, keeping the selection balanced.

## Key Features
Weighted lottery spins 
- Randomly selects a goal with bias towards less practiced ones.

Goal Management 
- Add and remove goals at any time.

Time logging 
- Log time sessions in increments per goal.

Persistent Storage 
- All goals and logged time are automatically saved before revealing the selected goal.
