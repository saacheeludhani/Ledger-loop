// Zero-dependency server (Node 18+): serves the site and proxies MiniMoth OTP calls.
// Run: node server.js   -> http://localhost:3000
const http=require('http'),fs=require('fs'),path=require('path');
const KEY=process.env.MINIMOTH_API_KEY||'mm_test_b68cbb0a1584567476f9c29c88bd08bc9b08d697c5cbca9babadacbe2549fe1c3a63e648cf609a7938231fde0b2966ab';
const MIME={'.html':'text/html; charset=utf-8','.txt':'text/plain','.xml':'application/xml'};
const ROUTES={'/api/otp/send':'/v1/otp/send','/api/otp/verify':'/v1/otp/verify'};
http.createServer(async(req,res)=>{
 const u=req.url.split('?')[0];
 if(req.method==='POST'&&ROUTES[u]){
  let b='';for await(const c of req)b+=c;
  try{const r=await fetch('https://api.minimoth.dev'+ROUTES[u],{method:'POST',headers:{'X-Api-Key':KEY,'Content-Type':'application/json'},body:b});
   res.writeHead(r.status,{'Content-Type':'application/json'});res.end(await r.text())}
  catch(e){res.writeHead(502,{'Content-Type':'application/json'});res.end(JSON.stringify({message:'Could not reach MiniMoth: '+e.message}))}
  return}
 const f=path.join(__dirname,u==='/'?'index.html':path.basename(u));
 fs.readFile(f,(e,d)=>{if(e){res.writeHead(404);return res.end('Not found')}
  res.writeHead(200,{'Content-Type':MIME[path.extname(f)]||'text/plain'});res.end(d)})
}).listen(process.env.PORT||3000,()=>console.log('LedgerLoop on http://localhost:'+(process.env.PORT||3000)));
