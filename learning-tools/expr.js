/** แปลงสูตร f(x) จากข้อความ เช่น x^2, y=x^2+1, sin(x) */
function compileExpr(raw) {
  let s = String(raw || '').trim().replace(/^y\s*=\s*/i, '');
  if (!s) throw new Error('กรุณาพิมพ์สูตร');

  if (/[`;{}[\]]|\\|=>/.test(s)) throw new Error('อักขระไม่รองรับ');
  if (/\b(function|return|while|for|eval|window|document|import|this)\b/i.test(s)) {
    throw new Error('สูตรไม่ถูกต้อง');
  }
  if (/[^0-9x+\-*/().,\s^a-zA-Z]/.test(s)) throw new Error('ใช้ได้เฉพาะ x ตัวเลข + − × ÷ ^ และ sin cos tan sqrt abs exp ln');

  s = s.replace(/\^/g, '**');
  s = s.replace(/\bexp\b/gi, 'Math.exp');
  s = s.replace(/\bsin\b/gi, 'Math.sin');
  s = s.replace(/\bcos\b/gi, 'Math.cos');
  s = s.replace(/\btan\b/gi, 'Math.tan');
  s = s.replace(/\bsqrt\b/gi, 'Math.sqrt');
  s = s.replace(/\babs\b/gi, 'Math.abs');
  s = s.replace(/\bln\b/gi, 'Math.log');
  s = s.replace(/\blog10\b/gi, 'Math.log10');
  s = s.replace(/\bpi\b/gi, 'Math.PI');
  s = s.replace(/\be\b/g, 'Math.E');
  s = s.replace(/(\d)\s*x\b/gi, '$1*x');
  s = s.replace(/\)\s*x\b/gi, ')*x');
  s = s.replace(/\bx\s*\(/gi, 'x*(');
  s = s.replace(/\)\s*\(/g, ')*(');

  const fn = new Function('x', '"use strict"; return (' + s + ');');
  return x => {
    try {
      const y = fn(x);
      return typeof y === 'number' && Number.isFinite(y) ? y : NaN;
    } catch (_) {
      return NaN;
    }
  };
}

/** อนุพันธ์เชิงตัวเลข (central difference) */
function numericalDerivative(f, a, h) {
  h = h || 1e-5;
  const y1 = f(a + h), y0 = f(a - h);
  if (!Number.isFinite(y1) || !Number.isFinite(y0)) return NaN;
  return (y1 - y0) / (2 * h);
}
