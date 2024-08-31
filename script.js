let previouslyRecommended = [];

function toggleLabelGroup(label, groupId) {
  const labels = document.querySelectorAll(`#${groupId} .custom-label`);
  
  labels.forEach(l => {
    if (l === label) {
      if (l.classList.contains('selected')) {
        l.classList.remove('selected'); // 이미 선택된 레이블이면 선택 해제
      } else {
        l.classList.add('selected');    // 선택되지 않은 레이블이면 선택 추가
      }
    } else {
      l.classList.remove('selected'); // 다른 레이블들은 선택 해제
    }
  });
}

// function recommendMenu() {
//   const selectedFeature = document.querySelector('.selected').getAttribute('data-feature');
//   const xhr = new XMLHttpRequest();
  
//   xhr.onreadystatechange = function() {
//     if (xhr.readyState == 4 && xhr.status == 200) {
//       const foodData = JSON.parse(xhr.responseText);
//       const filteredFood = foodData.filter(food => food.feature.includes(selectedFeature));
      
//       if (filteredFood.length > 0) {
//         const randomIndex = Math.floor(Math.random() * filteredFood.length);
//         const recommendedFood = filteredFood[randomIndex].name;
//         document.getElementById('recommended-menu').textContent = recommendedFood;
//       } else {
//         document.getElementById('recommended-menu').textContent = '추천할 음식이 없습니다.';
//       }
//     }
//   };
  
//   xhr.open('GET', 'foodData.json', true);
//   xhr.send();
// }

// function toggleLabelGroup(label, groupId) {
//   const labels = document.querySelectorAll(`#${groupId} .custom-label`);
  
//   labels.forEach(l => {
//     if (l === label) {
//       l.classList.toggle('selected'); // Toggle selection state
//     }
//   });
// }

function recommendMenu() {
  const selectedLabels = document.querySelectorAll('.custom-label.selected');
  const selectedFeatures = Array.from(selectedLabels).map(label => label.getAttribute('data-feature'));

  fetch('foodData.json')
    .then(response => response.json())
    .then(foodData => {
      const filteredFood = foodData.filter(food => {
        return selectedFeatures.every(feature => food.feature.includes(feature)) &&
               !previouslyRecommended.includes(food.name);
      });

      if (filteredFood.length > 0) {
        const randomIndex = Math.floor(Math.random() * filteredFood.length);
        const recommendedFood = filteredFood[randomIndex].name;
        document.getElementById('recommended-menu').textContent = recommendedFood;
        previouslyRecommended.push(recommendedFood);
      } else {
        document.getElementById('recommended-menu').textContent = '추천할 음식이 없습니다.';
      }
    })
    .catch(error => console.error('Error fetching food data:', error));
}