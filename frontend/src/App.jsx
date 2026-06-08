import { useEffect, useState } from "react";

function App() {

  const [reservas, setReservas] = useState([]);

  const [idUsuario, setIdUsuario] = useState("");
  const [idPista, setIdPista] = useState("");
  const [fecha, setFecha] = useState("");
  const [horaInicio, setHoraInicio] = useState("");
  const [horaFin, setHoraFin] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/reservas")
      .then(response => response.json())
      .then(data => setReservas(data));
  }, []);

  async function crearReserva() {

    const response = await fetch(
      "http://127.0.0.1:8000/reservas",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          id_usuario: Number(idUsuario),
          id_pista: Number(idPista),
          fecha: fecha,
          hora_inicio: horaInicio,
          hora_fin: horaFin
        })
      }
    );

    const data = await response.json();

    console.log(data);
  }

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