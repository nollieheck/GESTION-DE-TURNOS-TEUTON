import { useEffect, useState } from "react";

function App() {

  const [reservas, setReservas] = useState([]);
  const [usuarios, setUsuarios] = useState([]);
  const [pistas, setPistas] = useState([]);

  const [idUsuario, setIdUsuario] = useState("");
  const [idPista, setIdPista] = useState("");
  const [fecha, setFecha] = useState("");
  const [horaInicio, setHoraInicio] = useState("");
  const [horaFin, setHoraFin] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/reservas")
      .then(response => response.json())
      .then(data => setReservas(data));

    fetch("http://127.0.0.1:8000/usuarios")
      .then(response => response.json())
      .then(data => setUsuarios(data));

    fetch("http://127.0.0.1:8000/pistas")
      .then(response => response.json())
      .then(data => setPistas(data));
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

      <p>Usuarios: {usuarios.length}</p>
      <p>Pistas: {pistas.length}</p>


      {/* Muestra las reservas desde la mas reciente a la mas antigua */}

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

      <div>

        {/* Mostra la posiblidad de crear reservas */}

        <h2>Nueva Reserva</h2>

        {/*  Muestra los usuarios en un select para poder elegir */}

        <select
          value={idUsuario}
          onChange={(e) => setIdUsuario(e.target.value)}
        >
          <option value="">Seleccione un usuario</option>

          {usuarios.map(usuario => (
            <option
              key={usuario.id}
              value={usuario.id}
            >
              {usuario.nombre} {usuario.apellido}
            </option>
          ))}
        </select>

        <br /><br />

        {/*  Muestra las pistas en un select para poder elegir */}

        <select
          value={idPista}
          onChange={(e) => setIdPista(e.target.value)}
        >
          <option value="">Seleccione una pista</option>

          {pistas.map(pista => (
            <option
              key={pista.id}
              value={pista.id}
            >
              {pista.nombre}
            </option>
          ))}
        </select>

        <br /><br />

        <input
          type="date"
          value={fecha}
          onChange={(e) => setFecha(e.target.value)}
        />

        <br /><br />

        <input
          type="time"
          value={horaInicio}
          onChange={(e) => setHoraInicio(e.target.value)}
        />

        <br /><br />

        <input
          type="time"
          value={horaFin}
          onChange={(e) => setHoraFin(e.target.value)}
        />

        <br /><br />

        <button onClick={crearReserva}>
          Crear Reserva
        </button>
      </div>

      <hr />

    </div>
  );
}

export default App;