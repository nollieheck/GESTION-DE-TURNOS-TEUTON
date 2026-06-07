-- TABLA DE USUARIOS CON 10 USUSARIOS HARDCODEADOS --

CREATE TABLE Usuarios (
    IdUsuario INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    DNI VARCHAR(20),
    Telefono VARCHAR(20),
    Email VARCHAR(150) UNIQUE,
    FechaRegistro DATETIME DEFAULT GETDATE()
);

INSERT INTO Usuarios (Nombre, Apellido, DNI, Telefono, Email)
VALUES
('Juan', 'Perez', '30111222', '3514001001', 'juan.perez@gmail.com'),
('Maria', 'Gomez', '28456789', '3514001002', 'maria.gomez@gmail.com'),
('Lucas', 'Rodriguez', '32987456', '3514001003', 'lucas.rodriguez@gmail.com'),
('Sofia', 'Martinez', '35678901', '3514001004', 'sofia.martinez@gmail.com'),
('Nicolas', 'Lopez', '31123456', '3514001005', 'nicolas.lopez@gmail.com'),
('Valentina', 'Fernandez', '37890123', '3514001006', 'valentina.fernandez@gmail.com'),
('Agustin', 'Diaz', '34123456', '3514001007', 'agustin.diaz@gmail.com'),
('Camila', 'Torres', '36987654', '3514001008', 'camila.torres@gmail.com'),
('Franco', 'Ruiz', '33322111', '3514001009', 'franco.ruiz@gmail.com'),
('Julieta', 'Castro', '39222111', '3514001010', 'julieta.castro@gmail.com');

SELECT Nombre, Apellido, DNI
FROM dbo.Usuarios;

-- TABLA DE PISTAS CON DOS PISTAS HARDCODEADAS --

CREATE TABLE PISTAS (
    IdPista INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Activa BIT NOT NULL DEFAULT 1
);

INSERT INTO Pistas (Nombre, Activa)
VALUES
('Pista 1', 1),
('Pista 2', 0);

SELECT * FROM Pistas

DELETE FROM Pistas 
WHERE IdPista IN (3, 4);

-- TABLA DE RESERVAS CON 5 RESERVAS HARDCODEADAS --

CREATE TABLE Reservas (
    IdReserva INT IDENTITY(1,1) PRIMARY KEY,
    IdUsuario INT NOT NULL,
    IdPista INT NOT NULL,
    Fecha DATE NOT NULL,
    HoraInicio TIME NOT NULL,
    HoraFin TIME NOT NULL,
    Estado VARCHAR(20) NOT NULL DEFAULT 'RESERVADA',

    FOREIGN KEY (IdUsuario)
        REFERENCES Usuarios(IdUsuario),

    FOREIGN KEY (IdPista)
        REFERENCES Pistas(IdPista)
);

ALTER TABLE Reservas
ADD FechaCreacion DATETIME DEFAULT GETDATE();

ALTER TABLE Reservas
ADD CONSTRAINT UQ_ReservaHorario
UNIQUE (
    IdPista,
    Fecha,
    HoraInicio
);

INSERT INTO Reservas (IdUsuario, IdPista, Fecha, HoraInicio, HoraFin, Estado, FechaCreacion)
VALUES
(1, 1, '2026-06-10', '10:00:00', '11:00:00', 'RESERVADA', '2026-06-07'),
(2, 2, '2026-06-10', '11:00:00', '12:00:00', 'CONFIRMADA', '2026-06-04'),
(3, 1, '2026-06-10', '15:00:00', '16:00:00', 'RESERVADA', '2026-06-07'),
(4, 2, '2026-06-11', '17:00:00', '18:00:00', 'FINALIZADA', '2026-06-09'),
(5, 1, '2026-06-12', '19:00:00', '20:00:00', 'CANCELADA', '2026-06-05');

SELECT * FROM Reservas;

DELETE FROM Reservas 
WHERE IdReserva IN (1, 2, 3, 4, 5);

-- HISTORIAL DE RESERVAS --

CREATE TABLE HistorialReservas (
    IdHistorial INT IDENTITY(1,1) PRIMARY KEY,
    IdReserva INT NOT NULL,
    EstadoAnterior VARCHAR(20),
    EstadoNuevo VARCHAR(20),
    FechaCambio DATETIME DEFAULT GETDATE(),
    Observacion VARCHAR(255),

    FOREIGN KEY (IdReserva)
        REFERENCES Reservas(IdReserva)
);

-- TABLA DE HORARIOS BLOQUEADOS --

CREATE TABLE HorariosBloqueados (
    IdBloqueo INT IDENTITY(1,1) PRIMARY KEY,
    IdPista INT NOT NULL,
    Fecha DATE NOT NULL,
    HoraInicio TIME NOT NULL,
    HoraFin TIME NOT NULL,
    Motivo VARCHAR(255),

    FOREIGN KEY (IdPista)
        REFERENCES Pistas(IdPista)
);

-- TABLA DE PAGOS --

CREATE TABLE Pagos (
    IdPago INT IDENTITY(1,1) PRIMARY KEY,
    IdReserva INT NOT NULL,
    Monto DECIMAL(10,2) NOT NULL,
    MetodoPago VARCHAR(30),
    FechaPago DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (IdReserva)
        REFERENCES Reservas(IdReserva)
);

-- TABLA DE ADMINS --

CREATE TABLE Empleados (
    IdEmpleado INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Usuario VARCHAR(50),
    PasswordHash VARCHAR(255)
);

-- TABLA DE NOTIFICACIONES -- 

CREATE TABLE Notificaciones (
    IdNotificacion INT IDENTITY(1,1) PRIMARY KEY,
    IdUsuario INT NOT NULL,
    Mensaje VARCHAR(255),
    FechaEnvio DATETIME,
    Leida BIT DEFAULT 0,

    FOREIGN KEY (IdUsuario)
        REFERENCES Usuarios(IdUsuario)
);