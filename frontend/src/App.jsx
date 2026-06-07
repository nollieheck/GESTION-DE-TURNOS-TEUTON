import { useEffect, useState } from "react";

function App() {

  const [reservas, setReservas] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/reservas")
      .then(response => response.json())
      .then(data => setReservas(data));
  }, []);

  return (
    <div>
      <h1>Gestión de Turnos Teuton</h1>

      <h2>Reservas</h2>

      <ul>
        {reservas.map(reserva => (
          <li key={reserva.id_reserva}>
            Pista {reserva.id_pista} -
            {reserva.fecha} -
            {reserva.hora_inicio}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default App;