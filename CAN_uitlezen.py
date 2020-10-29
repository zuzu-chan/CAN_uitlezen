import socket
import struct

sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
sock.bind(("can0",))

fmt = "<IB3x8s"

while True:
  can_pkt = sock.recv(16)

  can_id, length, data = struct.unpack(fmt, can_pkt)
  can_id &= socket.CAN_EFF_MASK
  data = data[:length]
  y_sin = (data[0]) | (data[1] << 8) | (data[2] << 16) | (data[3] << 24)
  print("ID: {:#04x} Length: {} y_sin: {}".format(can_id, length, y_sin))
