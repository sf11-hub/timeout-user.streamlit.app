import streamlit as st
import os
from dataclasses import dataclass
# @st.cache_data
# def get_timeout():
#   return timeout_seconds
from dataclasses_json import dataclass_json, LetterCase

from queue import Queue
from utils.thread import keepAlive

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(slots=True)
class App:
  queue: Queue = Queue()
  _timeout: int = 1


  def __post_init__(self):
    print("creating new app instance")
  
  @property
  def timeout_ms(self):
    return self.timeout*1000  
  
  @property
  def timeout(self):
    return self._timeout
  
  @timeout.setter
  def timeout(self, value):      
    
    timeout_changed = self._timeout != value
    
    print(self._timeout, value)
    
    if not timeout_changed:
      print("timeout not changed")
      return
    
    self._timeout = value
    # self.queue.put(value)
    print("rerun after setting timeout")
    st.rerun()
    

def onchange( ):
  # cannot pass st.rerun in callback
  f"Timeout after user inactivity of {app.timeout} seconds"
  
  print("reruns depreacted timeout")
  
  
  
app = st.session_state.get('app', App())

app.timeout = st.sidebar.slider("Set Timeout (seconds)", 1, 300, value=app.timeout, key="timeout_seconds",on_change=onchange)


script_path = os.path.join('static', 'timeout.js')

with open(script_path) as f1:
  script_content = f1.read()
  script_content.replace('1000', f'{app.timeout}')
  st.markdown(f"<script> {f1.read()}</script>", unsafe_allow_html=True)