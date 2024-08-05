const Update = (id) => {
    let spanUpdate = document.querySelector(`.spanUpdate${id}`);
    let spanSubmit = document.querySelector(`.spanSubmit${id}`);
    let spanUpdateCancel = document.querySelector(`.spanUpdateCancel${id}`);
    let selectDate = document.querySelector(`.selectDate${id}`);
    let selectTime = document.querySelector(`.selectTime${id}`);
  
    console.log(spanUpdate);
    spanUpdate.style.display = 'none';
    selectDate.style.display = 'inline-block';
    selectTime.style.display = 'inline-block';
    spanSubmit.style.display = 'inline-block';
    spanUpdateCancel.style.display = 'inline-block';
}