// Loader to create SVG path for the orbs to travel along
window.onload = () => {
  const reductionRatio = 100;
  const map = $('#map');
  const mapHeight = map.height() - reductionRatio;
  const mapWidth = map.width() - reductionRatio;

  $('.orb').css('offsetPath', `path("M ${reductionRatio},${reductionRatio} L ${mapWidth}, ${reductionRatio} L ${mapWidth},${mapHeight} L ${reductionRatio},${mapHeight} Z")`);

  setTimeout(() => {
    $('.blue-orb').css('animationPlayState', 'running');
    $('.blue-orb').css('animationDelay', '-6s');
    $('.blue-orb.top-orb').css('animationPlayState', 'running');
    $('.blue-orb.top-orb').css('animationDelay', '-10s !important');
    $('.purple-orb').css('animationPlayState', 'running');
    $('.purple-orb').css('animationDelay', '-6s !important');
  }, 3000);
};

function loadMap() {
  // Edit this list according to the places you visited
  const visitedPlaces = [
    {
      latitude: 37.7829,
      longitude: -122.4190,
      label: "San Francisco",
      tooltip: `Love this city!`
    },
    {
      latitude: 34.073810,
      longitude: -118.361500,
      label: "Los Angeles",
      tooltip: `Love the hollywood vibe! 🎬`
    },
    {
      latitude: 32.728822,
      longitude: -117.129873,
      label: "San Diego",
      tooltip: `Awesome Museums!`
    },
    {
      latitude: 37.335930,
      longitude: -121.880941,
      label: "San José",
      tooltip: `Love this city!`
    },
    {
      latitude: 36.176705,
      longitude: -115.183962,
      label: "Las Vegas",
      tooltip: ``
    },
    {
      latitude: 33.474199,
      longitude: -112.058438,
      label: "Phoenix",
      tooltip: ``
    },
    {
      latitude: 32.762952,
      longitude: -96.791899,
      label: "Dallas",
      tooltip: ``
    },
    {
      latitude: 30.258370,
      longitude: -97.728249,
      label: "Austin",
      tooltip: ``
    },
    {
      latitude: 29.422478,
      longitude: -98.496419,
      label: "San Antonio",
      tooltip: ``
    },
    {
      latitude: 29.749759,
      longitude: -95.388467,
      label: "Houston",
      tooltip: ``
    },
    {
      latitude: 29.948853,
      longitude: -90.074512,
      label: "New Orleans",
      tooltip: ``
    },
    {
      latitude: 28.512444,
      longitude: -81.373094,
      label: "Orlando",
      tooltip: ``
    },
    {
      latitude: 38.903663,
      longitude: -77.023837,
      label: "Washington DC",
      tooltip: ``
    },
    {
      latitude: 40.747863,
      longitude: -73.985578,
      label: "NYC",
      tooltip: ``
    },
    {
      latitude: 22.892709,
      longitude: -109.914497,
      label: "Cabo San Lucas",
      tooltip: `Loved this trip with my family!`
    },
    {
      latitude: 19.427491,
      longitude: -99.132479,
      label: "Ciudad de México",
      tooltip: ``
    },
    {
      latitude: 26.195358,
      longitude: -98.230660,
      label: "McAllen",
      tooltip: ``
    },
    {
      latitude: 26.088082,
      longitude: -98.273706,
      label: "Reynosa",
      tooltip: `👶🏻 I was born here!`
    },
    {
      latitude: 25.652277,
      longitude: -100.276515,
      label: "Monterrey",
      tooltip: `📓 I study here!`
    },
    {
      latitude: 20.964114,
      longitude: -89.593342,
      label: "Mérida",
      tooltip: ``
    },
    {
      latitude: 21.158634,
      longitude: -86.849843,
      label: "Cancún",
      tooltip: `Not a fan of the beach!`
    },
    {
      latitude: 16.969091,
      longitude: -93.116547,
      label: "Chiapas",
      tooltip: ``
    },
    {
      latitude: 16.969091,
      longitude: -93.116547,
      label: "Huatulco",
      tooltip: ``
    },
    {
      latitude: 20.867783,
      longitude: -101.154307,
      label: "Guanajuato",
      tooltip: ``
    },
    {
      latitude: 20.650315,
      longitude: -103.348724,
      label: "Guadalajara",
      tooltip: ``
    },
    {
      latitude: 19.055931,
      longitude: -98.201551,
      label: "Puebla",
      tooltip: ``
    },
    {
      latitude: 40.404280,
      longitude: -3.685600,
      label: "Madrid",
      tooltip: ``
    },
    {
      latitude: 41.385240,
      longitude: -2.169015,
      label: "Barcelona",
      tooltip: ``
    },
    {
      latitude: 48.855414,
      longitude: -2.358475,
      label: "Paris",
      tooltip: ``
    },
    {
      latitude: 52.333168,
      longitude: 4.875968,
      label: "Amsterdam",
      tooltip: ``
    },
    {
      latitude: 50.844042,
      longitude: 4.354181,
      label: "Brussels",
      tooltip: ``
    },
    {
      latitude: 51.518135,
      longitude: -0.129729,
      label: "London",
      tooltip: ``
    },
    {
      latitude: 48.135025,
      longitude: 11.564423,
      label: "Munich",
      tooltip: ``
    },
    {
      latitude: 52.519015,
      longitude: 13.408390,
      label: "Berlin",
      tooltip: ``
    },
    {
      latitude: 53.546819,
      longitude: 9.987812,
      label: "Hamburg",
      tooltip: ``
    },
  ]
  
  Mapkick.options = {
    style:'../static/mapStyles/dark_theme.json', 
    zoom: 0.9, 
    center: [0, 40],
    tooltips: {html: true, hover: true},
    markers: {color: "#f84d4d"},
    label: {color: "#f84d4d"},
    textColor: "#f84d4d"
  };

  new Mapkick.Map("map", visitedPlaces);
}