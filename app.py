import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cờ Vua — Royal Clash", page_icon="♟️", layout="wide")

HTML = r"""
<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
<style>
:root{--bg:#101521;--panel:#192233;--gold:#f5c451;--text:#f5f7fb;--muted:#aab5c8}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(circle at top,#26344d 0,#101521 58%);color:var(--text);font-family:Inter,Segoe UI,Arial,sans-serif}
.wrap{max-width:1120px;margin:0 auto;padding:20px}
.hero{min-height:78vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.logo{font-size:clamp(48px,9vw,88px);line-height:1;margin-bottom:14px;filter:drop-shadow(0 8px 20px #0008)}
h1{font-size:clamp(34px,6vw,62px);letter-spacing:3px;margin:8px 0;color:#fff}
.sub{color:var(--muted);font-size:18px;max-width:600px;line-height:1.6}
.btn{border:0;border-radius:13px;padding:13px 20px;font-weight:800;font-size:16px;cursor:pointer;transition:.18s transform,.18s filter}
.btn:hover{transform:translateY(-2px);filter:brightness(1.08)}
.primary{background:linear-gradient(135deg,#ffe08a,#e9a923);color:#201805;box-shadow:0 8px 25px #d89b2933}
.secondary{background:#29364b;color:#f4f7ff;border:1px solid #3a4b65}
.startbtn{margin-top:28px;min-width:190px;font-size:19px}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;width:min(760px,100%);margin-top:30px}
.modecard{background:linear-gradient(145deg,#202d42,#151d2c);border:1px solid #35435a;border-radius:20px;padding:28px 20px;cursor:pointer;text-align:left;transition:.2s}
.modecard:hover{border-color:var(--gold);transform:translateY(-3px)}
.modeicon{font-size:40px}.modecard h2{margin:12px 0 8px}.modecard p{color:var(--muted);line-height:1.5;margin-bottom:0}
.game{display:none}.topbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px;flex-wrap:wrap}
.brand{font-weight:900;letter-spacing:1.5px;font-size:22px}.brand span{color:var(--gold)}
.layout{display:grid;grid-template-columns:minmax(280px, min(68vh, 650px)) minmax(260px,1fr);gap:22px;align-items:start}
.boardpanel,.sidepanel{background:#192233d9;border:1px solid #34435a;border-radius:18px;padding:14px;box-shadow:0 18px 50px #0003}
#board{width:100%;max-width:650px;margin:auto}
.sidepanel{padding:20px}.status{padding:13px 14px;background:#101725;border-radius:12px;font-weight:800;margin-bottom:14px;border:1px solid #303d52}
.status small{display:block;color:var(--muted);font-weight:500;margin-top:5px}
.actions{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 18px}.actions .btn{font-size:14px;padding:10px 13px}
.moves{height:220px;overflow:auto;background:#101725;border-radius:12px;padding:12px;color:#dce4f2;line-height:1.9;font-family:ui-monospace,monospace}
.help{color:var(--muted);font-size:13px;line-height:1.6;margin-top:14px}
.settings{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 14px;padding:12px;background:#101725;border:1px solid #303d52;border-radius:12px}.settings label{font-size:14px;color:var(--muted);font-weight:700}.settings select{background:#29364b;color:#fff;border:1px solid #50617a;border-radius:8px;padding:9px;font-size:14px}.settings .btn{padding:9px 12px;font-size:13px}
.square-55d63{position:relative}
.white-1e1d7{background:#f0d9b5!important}.black-3c85d{background:#b58863!important}
.highlight{box-shadow:inset 0 0 0 5px #f6d34d, inset 0 0 0 9px #f6d34d55!important;z-index:2}
.dot:after{content:"";position:absolute;width:22%;height:22%;left:39%;top:39%;border-radius:50%;background:#176b43d9;box-shadow:0 0 0 2px #f5f7fb99;pointer-events:none;z-index:20}
.capture:after{content:"";position:absolute;inset:4px;border:5px solid #176b43e8;border-radius:50%;box-shadow:inset 0 0 0 2px #f5f7fb88;pointer-events:none;z-index:20}
@media(max-width:800px){.layout{grid-template-columns:1fr}.boardpanel{padding:8px}.sidepanel{padding:15px}.cards{grid-template-columns:1fr}.wrap{padding:12px}}
</style>
</head>
<body>
<div class="wrap">
  <section id="welcome" class="hero">
    <div class="logo">♔ ♛</div>
    <h1>CỜ VUA</h1>
    <div class="sub">ROYAL CLASH · Đấu trí từng nước đi.<br>Chọn chế độ chơi và bắt đầu trận đấu.</div>
    <button class="btn primary startbtn" id="start">CHƠI NGAY　➜</button>
  </section>
  <section id="choose" class="hero" style="display:none">
    <div class="logo">♞</div><h1>CHỌN CHẾ ĐỘ</h1>
    <div class="sub">Mày muốn thử sức với máy hay đấu trực tiếp với bạn?</div>
    <div class="cards">
      <button class="modecard" id="vsai"><div class="modeicon">🤖</div><h2>Chơi với AI</h2><p>Đến lượt mày đi quân Trắng. Máy sẽ tự đi quân Đen.</p></button>
      <button class="modecard" id="vsfriend"><div class="modeicon">♟️</div><h2>Hai người chơi</h2><p>Hai người thay phiên nhau đi trên cùng một bàn cờ.</p></button>
    </div>
    <button class="btn secondary" id="backWelcome" style="margin-top:24px">← Quay lại</button>
  </section>
  <section id="game" class="game">
    <div class="topbar"><div class="brand">♔ <span>ROYAL</span> CLASH</div><button class="btn secondary" id="menu">⌂ Menu</button></div>
    <div class="layout">
      <div class="boardpanel"><div id="board"></div></div>
      <div class="sidepanel">
        <div class="status" id="status">Trắng đi trước<small>Chọn một quân cờ để xem các nước có thể đi.</small></div>
        <div class="settings" id="aiSettings"><label for="difficulty">🤖 Độ khó AI</label><select id="difficulty"><option value="easy">Dễ</option><option value="medium" selected>Trung bình</option><option value="hard">Khó</option></select></div>
        <div class="settings"><button class="btn secondary" id="musicBtn">♫ Bật nhạc</button><span style="color:var(--muted);font-size:13px">Nhạc nền và âm báo nước đi</span></div>
        <div class="actions">
          <button class="btn primary" id="undo">↶ Đi lại</button>
          <button class="btn secondary" id="restart">⟳ Chơi lại</button>
          <button class="btn secondary" id="flip">⇅ Đổi góc nhìn</button>
        </div>
        <h3>📜 Lịch sử nước đi</h3><div class="moves" id="moves">Chưa có nước đi nào.</div>
        <div class="help">• Ô có chấm xanh là nước đi hợp lệ.<br>• Vòng tròn xanh báo có thể ăn quân.<br>• Nước đi sai luật sẽ không được thực hiện.<br>• Khi quân bị ăn, quân đó sẽ biến mất khỏi bàn cờ.</div>
      </div>
    </div>
  </section>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>
<script>
let game = new Chess(), board = null, mode = 'ai', selected = null, aiBusy = false;
let audioCtx=null, musicTimer=null, musicOn=false, melodyStep=0;
const melody=[261.63,329.63,392,329.63,293.66,349.23,440,349.23,261.63,329.63,392,523.25,440,392,329.63,293.66];
const $ = id => document.getElementById(id);
function show(id){['welcome','choose','game'].forEach(x=>$(x).style.display=x===id?(x==='game'?'block':'flex'):'none');}
$('start').onclick=()=>show('choose');
$('backWelcome').onclick=()=>show('welcome');
$('vsai').onclick=()=>startGame('ai');
$('vsfriend').onclick=()=>startGame('friend');
$('menu').onclick=()=>{if(board){board.destroy();board=null}show('choose')};
function startGame(m){mode=m;game=new Chess();selected=null;aiBusy=false;show('game');$('aiSettings').style.display=m==='ai'?'flex':'none';if(board)board.destroy();board=Chessboard('board',{position:'start',draggable:true,moveSpeed:180,pieceTheme:'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',onDragStart,onDrop,onSnapEnd});board.resize();render();setTimeout(()=>window.dispatchEvent(new Event('resize')),50);}
function onDragStart(source,piece){if(game.game_over()||aiBusy)return false;if(mode==='ai'&&piece[0]==='b')return false;return true;}
function onDrop(source,target){clearMarks();let move=game.move({from:source,to:target,promotion:'q'});if(move===null){render();return 'snapback'}playMoveSound(!!move.captured);selected=null;render();if(mode==='ai'&&game.turn()==='b'&&!game.game_over())setTimeout(aiMove,300);}
function onSnapEnd(){board.position(game.fen());}
function clearMarks(){document.querySelectorAll('#board .square-55d63').forEach(s=>s.classList.remove('highlight','dot','capture'));}
function markSquare(sq,cls){let el=document.querySelector('#board .square-'+sq);if(el)el.classList.add(cls);}
function onSquareClick(square){if(!board||game.game_over()||aiBusy)return;if(mode==='ai'&&game.turn()==='b')return;const piece=game.get(square);if(selected){let moves=game.moves({square:selected,verbose:true});let chosen=moves.find(m=>m.to===square);if(chosen){let played=game.move({from:selected,to:square,promotion:'q'});playMoveSound(!!(played&&played.captured));selected=null;clearMarks();render();if(mode==='ai'&&game.turn()==='b'&&!game.game_over())setTimeout(aiMove,300);return;}}
if(piece&&piece.color===game.turn()){selected=square;clearMarks();markSquare(square,'highlight');game.moves({square,verbose:true}).forEach(m=>markSquare(m.to,m.captured?'capture':'dot'));}else{selected=null;clearMarks();}}
function pieceValue(type){return ({p:100,n:320,b:330,r:500,q:900,k:20000})[type]||0;}
function evaluate(){if(game.in_checkmate())return game.turn()==='b'?-100000:100000;if(game.in_draw())return 0;let score=0;for(let r=0;r<8;r++)for(let f=0;f<8;f++){let sq='abcdefgh'[f]+(8-r),p=game.get(sq);if(!p)continue;let v=pieceValue(p.type);let center=3.5-(Math.abs(3.5-f)+Math.abs(3.5-r))/2;v+=p.type==='p'?((p.color==='w'?6-r:r-1)*4):center*4;score+=(p.color==='b'?v:-v);}return score;}
function minimax(depth,alpha,beta,maximizing){if(depth===0||game.game_over())return evaluate();let moves=game.moves({verbose:true});moves.sort((a,b)=>((b.captured?pieceValue(b.captured):0)-(a.captured?pieceValue(a.captured):0)));if(maximizing){let best=-Infinity;for(let m of moves){game.move({from:m.from,to:m.to,promotion:'q'});let val=minimax(depth-1,alpha,beta,false);game.undo();best=Math.max(best,val);alpha=Math.max(alpha,best);if(beta<=alpha)break;}return best;}else{let best=Infinity;for(let m of moves){game.move({from:m.from,to:m.to,promotion:'q'});let val=minimax(depth-1,alpha,beta,true);game.undo();best=Math.min(best,val);beta=Math.min(beta,best);if(beta<=alpha)break;}return best;}}
function aiMove(){if(game.game_over()||mode!=='ai'||game.turn()!=='b')return;aiBusy=true;render();setTimeout(()=>{let moves=game.moves({verbose:true});if(!moves.length){aiBusy=false;render();return;}let level=$('difficulty').value;let depth=level==='easy'?1:level==='medium'?2:3;let chosen;if(level==='easy'){moves.sort(()=>Math.random()-.5);chosen=moves[0];}else{let best=-Infinity,candidates=[];for(let m of moves){game.move({from:m.from,to:m.to,promotion:'q'});let val=minimax(depth-1,-Infinity,Infinity,false);game.undo();if(val>best){best=val;candidates=[m];}else if(val===best)candidates.push(m);}chosen=candidates[Math.floor(Math.random()*candidates.length)];}let played=game.move({from:chosen.from,to:chosen.to,promotion:'q'});playMoveSound(!!(played&&played.captured));aiBusy=false;selected=null;clearMarks();render();},30);}
function ensureAudio(){if(!audioCtx)audioCtx=new (window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
function tone(freq,duration,volume=.035,type='sine'){let ctx=ensureAudio(),osc=ctx.createOscillator(),gain=ctx.createGain();osc.type=type;osc.frequency.value=freq;gain.gain.setValueAtTime(volume,ctx.currentTime);gain.gain.exponentialRampToValueAtTime(.001,ctx.currentTime+duration);osc.connect(gain);gain.connect(ctx.destination);osc.start();osc.stop(ctx.currentTime+duration);}
function musicTick(){if(!musicOn)return;tone(melody[melodyStep%melody.length],.42,.012,'triangle');if(melodyStep%4===0)tone(melody[(melodyStep+4)%melody.length]/2,.65,.009,'sine');melodyStep++;}
function toggleMusic(){if(!musicOn){ensureAudio();musicOn=true;musicTick();musicTimer=setInterval(musicTick,460);$('musicBtn').textContent='♫ Tắt nhạc';}else{musicOn=false;clearInterval(musicTimer);musicTimer=null;$('musicBtn').textContent='♫ Bật nhạc';}}
function playMoveSound(capture){try{tone(capture ? 180 : 440, capture ? .22 : .11, capture ? .055 : .025, capture ? 'square' : 'sine');}catch(e){}}
$('musicBtn').onclick=toggleMusic;
function render(){if(board)board.position(game.fen());clearMarks();$('status').innerHTML=statusText();let hist=game.history();if(!hist.length){$('moves').textContent='Chưa có nước đi nào.';}else{let rows=[];for(let i=0;i<hist.length;i+=2)rows.push((Math.floor(i/2)+1)+'. '+hist[i]+(hist[i+1]?'　'+hist[i+1]:''));$('moves').textContent=rows.join('\\n');$('moves').style.whiteSpace='pre-wrap';$('moves').scrollTop=$('moves').scrollHeight;}if(board){if(!window.squareClickBound){$('board').addEventListener('click',e=>{let el=e.target.closest('.square-55d63');if(!el)return;let match=el.className.match(/square-([a-h][1-8])/);if(match)onSquareClick(match[1]);});window.squareClickBound=true;}}}
function statusText(){if(game.in_checkmate())return '♚ Chiếu hết! '+(game.turn()==='w'?'Đen':'Trắng')+' thắng.';if(game.in_stalemate()||game.in_draw())return '🤝 Ván cờ hòa.';let who=game.turn()==='w'?'Trắng':'Đen';let extra=game.in_check()?' · ĐANG BỊ CHIẾU':'';if(aiBusy)return '🤖 AI đang suy nghĩ...<small>Chờ máy hoàn tất nước đi.</small>';return who+' đi'+extra+'<small>'+(mode==='ai'?'Chế độ: Chơi với AI · Độ khó: '+({'easy':'Dễ','medium':'Trung bình','hard':'Khó'}[$('difficulty').value]):'Chế độ: Hai người chơi')+'</small>';}
$('undo').onclick=()=>{if(aiBusy)return;game.undo();if(mode==='ai'&&game.turn()==='b')game.undo();selected=null;render();};
$('difficulty').onchange=()=>render();
$('restart').onclick=()=>{game.reset();selected=null;aiBusy=false;render();};
$('flip').onclick=()=>{if(board){board.flip();setTimeout(()=>board.resize(),30)}};
window.addEventListener('resize',()=>{if(board)board.resize()});
</script>
</body></html>
"""
components.html(HTML, height=1000, scrolling=True)
