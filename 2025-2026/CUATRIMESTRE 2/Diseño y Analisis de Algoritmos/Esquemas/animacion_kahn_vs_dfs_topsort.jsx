import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Slider } from "@/components/ui/slider";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Play, Pause, RotateCcw, SkipBack, SkipForward } from "lucide-react";

const nodes = [0, 1, 2, 3, 4];
const edges = [
  [0, 2],
  [2, 4],
  [0, 1],
  [1, 2],
  [0, 4],
  [2, 3],
];

const positions = {
  0: { x: 80, y: 160 },
  1: { x: 250, y: 80 },
  2: { x: 250, y: 240 },
  3: { x: 450, y: 280 },
  4: { x: 450, y: 120 },
};

const pythonKahn = [
  "from collections import deque",
  "",
  "def kahn_toposort(n, edges):",
  "    graph = [[] for _ in range(n)]",
  "    indeg = [0] * n",
  "    for u, v in edges:",
  "        graph[u].append(v)",
  "        indeg[v] += 1",
  "",
  "    q = deque()",
  "    for i in range(n):",
  "        if indeg[i] == 0:",
  "            q.append(i)",
  "",
  "    order = []",
  "    while q:",
  "        u = q.popleft()",
  "        order.append(u)",
  "        for v in graph[u]:",
  "            indeg[v] -= 1",
  "            if indeg[v] == 0:",
  "                q.append(v)",
  "",
  "    return order if len(order) == n else None",
];

const pythonDFS = [
  "def dfs_toposort(n, edges):",
  "    graph = [[] for _ in range(n)]",
  "    for u, v in edges:",
  "        graph[u].append(v)",
  "",
  "    visited = [0] * n  # 0=blanco, 1=gris, 2=negro",
  "    postorder = []",
  "",
  "    def dfs(u):",
  "        visited[u] = 1",
  "        for v in graph[u]:",
  "            if visited[v] == 0:",
  "                dfs(v)",
  "        visited[u] = 2",
  "        postorder.append(u)",
  "",
  "    for i in range(n):",
  "        if visited[i] == 0:",
  "            dfs(i)",
  "",
  "    postorder.reverse()",
  "    return postorder",
];

function clone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

function buildAdjacency() {
  const g = Object.fromEntries(nodes.map((n) => [n, []]));
  for (const [u, v] of edges) g[u].push(v);
  return g;
}

function buildIndeg() {
  const indeg = Object.fromEntries(nodes.map((n) => [n, 0]));
  for (const [, v] of edges) indeg[v] += 1;
  return indeg;
}

function nodeColorsForDFS(state) {
  const map = {};
  for (const n of nodes) {
    const v = state.visited?.[n] ?? 0;
    map[n] = v === 0 ? "white" : v === 1 ? "gray" : "black";
  }
  return map;
}

function generateKahnSteps() {
  const g = buildAdjacency();
  const indeg = buildIndeg();
  const q = [];
  const order = [];
  const steps = [];

  const pushStep = (extra) => {
    steps.push({
      ...extra,
      indeg: clone(indeg),
      queue: [...q],
      order: [...order],
    });
  };

  pushStep({
    line: 3,
    title: "Inicialización",
    explanation:
      "Se crean la lista de adyacencia y el vector de grados de entrada. El grado de entrada de cada nodo cuenta cuántas aristas llegan a él.",
    activeNodes: [],
    activeEdges: [],
    variables: {
      graph: JSON.stringify(g),
      indeg: JSON.stringify(indeg),
    },
  });

  for (const n of nodes) {
    pushStep({
      line: 10,
      title: "Búsqueda de nodos fuente",
      explanation:
        `Se examina el nodo ${n}. Si su grado de entrada es 0, puede entrar en la cola porque no depende de ningún otro nodo.`,
      activeNodes: [n],
      activeEdges: [],
      variables: { checkingNode: n, indegNode: indeg[n] },
    });
    if (indeg[n] === 0) {
      q.push(n);
      pushStep({
        line: 12,
        title: "Nodo añadido a la cola",
        explanation:
          `El nodo ${n} tiene indegree 0, así que se añade a la cola. En Kahn, la cola contiene los nodos que ya se pueden procesar.`,
        activeNodes: [n],
        activeEdges: [],
        variables: { pushed: n },
      });
    }
  }

  while (q.length) {
    const u = q.shift();
    pushStep({
      line: 16,
      title: "Extraer de la cola",
      explanation:
        `Se extrae ${u} de la cola. Ese nodo ya puede fijarse en el orden topológico.`,
      activeNodes: [u],
      activeEdges: [],
      variables: { popped: u },
    });

    order.push(u);
    pushStep({
      line: 17,
      title: "Añadir al resultado",
      explanation:
        `Se añade ${u} al orden topológico parcial. El orden actual es [${order.join(", ")}].`,
      activeNodes: [u],
      activeEdges: [],
      variables: { order: `[${order.join(", ")}]` },
    });

    for (const v of g[u]) {
      indeg[v] -= 1;
      pushStep({
        line: 19,
        title: "Eliminar efecto de una arista",
        explanation:
          `Se procesa la arista ${u} → ${v}. Como ${u} ya está resuelto, el grado de entrada de ${v} disminuye a ${indeg[v]}.`,
        activeNodes: [u, v],
        activeEdges: [[u, v]],
        variables: { edge: `${u} -> ${v}`, indegUpdated: JSON.stringify(indeg) },
      });
      if (indeg[v] === 0) {
        q.push(v);
        pushStep({
          line: 20,
          title: "Nuevo nodo disponible",
          explanation:
            `El nodo ${v} ha quedado con indegree 0, así que ahora puede añadirse a la cola.`,
          activeNodes: [v],
          activeEdges: [[u, v]],
          variables: { pushed: v },
        });
      }
    }
  }

  pushStep({
    line: 23,
    title: "Resultado final de Kahn",
    explanation:
      `La cola queda vacía y el orden final es [${order.join(", ")}]. Como se procesaron los ${nodes.length} nodos, el grafo es acíclico y el orden es válido.`,
    activeNodes: [...order],
    activeEdges: [],
    variables: { finalOrder: `[${order.join(", ")}]` },
  });

  return steps;
}

function generateDFSSteps() {
  const g = buildAdjacency();
  const visited = Object.fromEntries(nodes.map((n) => [n, 0]));
  const postorder = [];
  const stack = [];
  const steps = [];

  const pushStep = (extra) => {
    steps.push({
      ...extra,
      visited: clone(visited),
      postorder: [...postorder],
      recursionStack: [...stack],
      nodeColors: nodeColorsForDFS({ visited }),
    });
  };

  pushStep({
    line: 1,
    title: "Construcción del grafo",
    explanation:
      "DFS también construye la lista de adyacencia, pero no necesita indegrees. Su idea es profundizar y registrar el postorden.",
    activeNodes: [],
    activeEdges: [],
    variables: { graph: JSON.stringify(g) },
  });

  function dfs(u) {
    visited[u] = 1;
    stack.push(u);
    pushStep({
      line: 9,
      title: "Entrar en DFS(u)",
      explanation:
        `Se entra en dfs(${u}). El nodo pasa a gris: está en exploración activa dentro de la pila de recursión.`,
      activeNodes: [u],
      activeEdges: [],
      variables: { entered: u },
    });

    for (const v of g[u]) {
      pushStep({
        line: 10,
        title: "Explorar vecino",
        explanation:
          `Desde ${u} se examina el vecino ${v}. Si ${v} está blanco, DFS profundiza en él antes de cerrar ${u}.`,
        activeNodes: [u, v],
        activeEdges: [[u, v]],
        variables: { edge: `${u} -> ${v}`, stateOfV: visited[v] },
      });
      if (visited[v] === 0) {
        pushStep({
          line: 11,
          title: "Llamada recursiva",
          explanation:
            `El nodo ${v} está blanco, así que se hace dfs(${v}).`,
          activeNodes: [u, v],
          activeEdges: [[u, v]],
          variables: { call: `dfs(${v})` },
        });
        dfs(v);
      }
    }

    visited[u] = 2;
    stack.pop();
    pushStep({
      line: 12,
      title: "Nodo completado",
      explanation:
        `Todos los descendientes de ${u} ya fueron explorados. El nodo pasa a negro: queda completamente procesado.`,
      activeNodes: [u],
      activeEdges: [],
      variables: { finished: u },
    });

    postorder.push(u);
    pushStep({
      line: 13,
      title: "Añadir a postorder",
      explanation:
        `Se añade ${u} al final del postorden. En DFS TopSort, el orden topológico se obtiene invirtiendo este vector al final.`,
      activeNodes: [u],
      activeEdges: [],
      variables: { postorder: `[${postorder.join(", ")}]` },
    });
  }

  for (const i of nodes) {
    pushStep({
      line: 15,
      title: "Bucle principal de nodos",
      explanation:
        `Se revisa el nodo ${i}. Si sigue blanco, se lanza una nueva DFS desde él.`,
      activeNodes: [i],
      activeEdges: [],
      variables: { checkingNode: i, color: visited[i] },
    });
    if (visited[i] === 0) {
      pushStep({
        line: 16,
        title: "Nueva componente DFS",
        explanation:
          `El nodo ${i} no ha sido visitado aún, así que comienza una exploración desde ese nodo.`,
        activeNodes: [i],
        activeEdges: [],
        variables: { startDFS: i },
      });
      dfs(i);
    }
  }

  const finalOrder = [...postorder].reverse();
  pushStep({
    line: 18,
    title: "Invertir el postorden",
    explanation:
      `El postorden es [${postorder.join(", ")}]. Al invertirlo obtenemos el orden topológico final: [${finalOrder.join(", ")}].`,
    activeNodes: [...finalOrder],
    activeEdges: [],
    variables: { finalOrder: `[${finalOrder.join(", ")}]` },
  });

  return steps;
}

const kahnSteps = generateKahnSteps();
const dfsSteps = generateDFSSteps();

function Arrow({ x1, y1, x2, y2, active }) {
  const dx = x2 - x1;
  const dy = y2 - y1;
  const len = Math.sqrt(dx * dx + dy * dy);
  const ux = dx / len;
  const uy = dy / len;
  const r = 26;
  const sx = x1 + ux * r;
  const sy = y1 + uy * r;
  const ex = x2 - ux * r;
  const ey = y2 - uy * r;

  return (
    <g>
      <line
        x1={sx}
        y1={sy}
        x2={ex}
        y2={ey}
        strokeWidth={active ? 4 : 2.5}
        className={active ? "stroke-blue-600" : "stroke-slate-400"}
        markerEnd="url(#arrowhead)"
      />
    </g>
  );
}

function GraphView({ step, mode }) {
  const activeEdges = new Set((step.activeEdges || []).map(([u, v]) => `${u}-${v}`));
  const activeNodes = new Set(step.activeNodes || []);
  const nodeColors = step.nodeColors || {};

  return (
    <Card className="rounded-2xl shadow-md">
      <CardHeader>
        <CardTitle>Grafo y estado visual</CardTitle>
      </CardHeader>
      <CardContent>
        <svg viewBox="0 0 530 360" className="w-full rounded-xl border bg-white">
          <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
              <polygon points="0 0, 10 3.5, 0 7" className="fill-slate-400" />
            </marker>
          </defs>

          {edges.map(([u, v]) => (
            <Arrow
              key={`${u}-${v}`}
              x1={positions[u].x}
              y1={positions[u].y}
              x2={positions[v].x}
              y2={positions[v].y}
              active={activeEdges.has(`${u}-${v}`)}
            />
          ))}

          {nodes.map((n) => {
            const isActive = activeNodes.has(n);
            const colorMode = mode === "dfs" ? nodeColors[n] : "default";
            const fill =
              colorMode === "gray"
                ? "#9ca3af"
                : colorMode === "black"
                ? "#111827"
                : isActive
                ? "#60a5fa"
                : "#f8fafc";
            const text = colorMode === "black" ? "#ffffff" : "#0f172a";
            const stroke = isActive ? "#2563eb" : "#475569";

            return (
              <motion.g key={n} initial={false} animate={{ scale: isActive ? 1.05 : 1 }}>
                <circle cx={positions[n].x} cy={positions[n].y} r="26" fill={fill} stroke={stroke} strokeWidth={isActive ? 4 : 2.5} />
                <text x={positions[n].x} y={positions[n].y + 5} textAnchor="middle" fontSize="18" fontWeight="700" fill={text}>
                  {n}
                </text>
              </motion.g>
            );
          })}
        </svg>

        <div className="mt-4 flex flex-wrap gap-2 text-sm">
          {mode === "kahn" ? (
            <>
              <Badge variant="secondary">Azul: nodo o arista activa</Badge>
              <Badge variant="secondary">Cola: [{(step.queue || []).join(", ")}]</Badge>
              <Badge variant="secondary">Orden: [{(step.order || []).join(", ")}]</Badge>
            </>
          ) : (
            <>
              <Badge variant="secondary">Blanco: no visitado</Badge>
              <Badge variant="secondary">Gris: en recursión</Badge>
              <Badge variant="secondary">Negro: terminado</Badge>
              <Badge variant="secondary">Pila recursiva: [{(step.recursionStack || []).join(", ")}]</Badge>
            </>
          )}
        </div>
      </CardContent>
    </Card>
  );
}

function CodeView({ lines, activeLine }) {
  return (
    <Card className="rounded-2xl shadow-md">
      <CardHeader>
        <CardTitle>Código Python animado</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="overflow-auto rounded-xl border bg-slate-950 p-4 font-mono text-sm text-slate-100">
          {lines.map((line, idx) => {
            const lineNo = idx + 1;
            const active = lineNo === activeLine;
            return (
              <div
                key={idx}
                className={`grid grid-cols-[40px_1fr] gap-4 rounded px-2 py-0.5 ${
                  active ? "bg-amber-400/20 ring-1 ring-amber-300" : ""
                }`}
              >
                <span className="text-slate-500">{lineNo}</span>
                <span className={active ? "text-amber-200" : "text-slate-200"}>{line || " "}</span>
              </div>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}

function VariablesView({ step, mode }) {
  return (
    <Card className="rounded-2xl shadow-md">
      <CardHeader>
        <CardTitle>Variables relevantes</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3 text-sm">
        {mode === "kahn" && (
          <>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">indegree</div>
              <div className="mt-1 font-mono">{JSON.stringify(step.indeg)}</div>
            </div>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">cola</div>
              <div className="mt-1 font-mono">[{(step.queue || []).join(", ")}]</div>
            </div>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">orden parcial</div>
              <div className="mt-1 font-mono">[{(step.order || []).join(", ")}]</div>
            </div>
          </>
        )}

        {mode === "dfs" && (
          <>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">visited (0 blanco, 1 gris, 2 negro)</div>
              <div className="mt-1 font-mono">{JSON.stringify(step.visited)}</div>
            </div>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">pila de recursión</div>
              <div className="mt-1 font-mono">[{(step.recursionStack || []).join(", ")}]</div>
            </div>
            <div className="rounded-xl border p-3">
              <div className="font-semibold">postorder</div>
              <div className="mt-1 font-mono">[{(step.postorder || []).join(", ")}]</div>
            </div>
          </>
        )}

        {step.variables && Object.keys(step.variables).length > 0 && (
          <div className="rounded-xl border bg-slate-50 p-3">
            <div className="mb-2 font-semibold">Detalle del paso</div>
            <div className="space-y-1 font-mono text-xs">
              {Object.entries(step.variables).map(([k, v]) => (
                <div key={k}>
                  <span className="font-bold">{k}</span>: {String(v)}
                </div>
              ))}
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
}

function ExplanationView({ step, stepIndex, totalSteps, mode }) {
  return (
    <Card className="rounded-2xl shadow-md">
      <CardHeader>
        <CardTitle>{mode === "kahn" ? "Explicación de Kahn" : "Explicación de DFS TopSort"}</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="flex flex-wrap items-center gap-2">
          <Badge>Paso {stepIndex + 1} / {totalSteps}</Badge>
          <Badge variant="secondary">{step.title}</Badge>
          <Badge variant="outline">Línea {step.line}</Badge>
        </div>
        <p className="text-sm leading-6 text-slate-700">{step.explanation}</p>
      </CardContent>
    </Card>
  );
}

function Controls({ playing, onPlayPause, onReset, onPrev, onNext, stepIndex, totalSteps, onSlider }) {
  return (
    <Card className="rounded-2xl shadow-md">
      <CardContent className="space-y-4 pt-6">
        <div className="flex flex-wrap items-center gap-2">
          <Button onClick={onPlayPause}>
            {playing ? <Pause className="mr-2 h-4 w-4" /> : <Play className="mr-2 h-4 w-4" />}
            {playing ? "Pausar" : "Reproducir"}
          </Button>
          <Button variant="outline" onClick={onPrev}><SkipBack className="mr-2 h-4 w-4" />Anterior</Button>
          <Button variant="outline" onClick={onNext}><SkipForward className="mr-2 h-4 w-4" />Siguiente</Button>
          <Button variant="ghost" onClick={onReset}><RotateCcw className="mr-2 h-4 w-4" />Reiniciar</Button>
        </div>
        <div className="space-y-2">
          <div className="text-sm text-slate-600">Posición de la animación: {stepIndex + 1} / {totalSteps}</div>
          <Slider value={[stepIndex]} min={0} max={Math.max(totalSteps - 1, 0)} step={1} onValueChange={(v) => onSlider(v[0])} />
        </div>
      </CardContent>
    </Card>
  );
}

function SummaryPanel() {
  return (
    <Card className="rounded-2xl shadow-md">
      <CardHeader>
        <CardTitle>Entrada del problema y conclusiones</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4 text-sm leading-6 text-slate-700">
        <div className="rounded-xl border bg-slate-50 p-3 font-mono text-xs text-slate-800">
          N = 5, M = 6\n
          0 → 2\n
          2 → 4\n
          0 → 1\n
          1 → 2\n
          0 → 4\n
          2 → 3
        </div>
        <p>
          En este DAG, tanto Kahn como DFS obtienen un orden topológico válido. En esta visualización concreta, ambos terminan en <strong>[0, 1, 2, 3, 4]</strong>, aunque podrían existir otros órdenes válidos dependiendo del orden en que se recorran nodos y vecinos.
        </p>
        <p>
          <strong>Diferencia conceptual:</strong> Kahn trabaja con nodos de indegree 0 y simula la eliminación progresiva de dependencias. DFS, en cambio, profundiza hasta el fondo y usa el postorden inverso para construir el resultado.
        </p>
      </CardContent>
    </Card>
  );
}

function usePlayer(totalSteps) {
  const [stepIndex, setStepIndex] = useState(0);
  const [playing, setPlaying] = useState(false);

  React.useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => {
      setStepIndex((prev) => {
        if (prev >= totalSteps - 1) {
          setPlaying(false);
          return prev;
        }
        return prev + 1;
      });
    }, 1800);
    return () => clearInterval(id);
  }, [playing, totalSteps]);

  const reset = () => {
    setPlaying(false);
    setStepIndex(0);
  };

  const next = () => setStepIndex((s) => Math.min(totalSteps - 1, s + 1));
  const prev = () => setStepIndex((s) => Math.max(0, s - 1));
  const slider = (value) => setStepIndex(value);

  return { stepIndex, setStepIndex, playing, setPlaying, reset, next, prev, slider };
}

function AlgorithmTab({ mode, steps, code }) {
  const player = usePlayer(steps.length);
  const step = steps[player.stepIndex];

  return (
    <div className="space-y-6">
      <Controls
        playing={player.playing}
        onPlayPause={() => player.setPlaying((p) => !p)}
        onReset={player.reset}
        onPrev={player.prev}
        onNext={player.next}
        stepIndex={player.stepIndex}
        totalSteps={steps.length}
        onSlider={player.slider}
      />

      <div className="grid gap-6 xl:grid-cols-[1.2fr_1fr]">
        <GraphView step={step} mode={mode} />
        <ExplanationView step={step} stepIndex={player.stepIndex} totalSteps={steps.length} mode={mode} />
      </div>

      <div className="grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
        <CodeView lines={code} activeLine={step.line} />
        <VariablesView step={step} mode={mode} />
      </div>
    </div>
  );
}

export default function App() {
  const comparison = useMemo(
    () => ({
      kahnOrder: kahnSteps[kahnSteps.length - 1].order,
      dfsOrder: [...dfsSteps[dfsSteps.length - 1].variables.finalOrder.replace(/[\[\]\s]/g, "").split(",")].filter(Boolean),
    }),
    []
  );

  return (
    <div className="min-h-screen bg-slate-100 p-4 md:p-8">
      <div className="mx-auto max-w-7xl space-y-6">
        <motion.div initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }}>
          <Card className="rounded-3xl shadow-lg">
            <CardContent className="p-6 md:p-8">
              <div className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
                <div>
                  <h1 className="text-3xl font-bold tracking-tight text-slate-900 md:text-4xl">
                    Animación didáctica: Kahn vs TopSort con DFS
                  </h1>
                  <p className="mt-3 max-w-3xl text-sm leading-6 text-slate-600 md:text-base">
                    Visualización paso a paso del ordenamiento topológico sobre el grafo dado. Incluye animación del grafo,
                    variables internas, explicación de cada transición y resaltado de las líneas del código Python que se están ejecutando.
                  </p>
                </div>
                <div className="grid gap-3 rounded-2xl border bg-slate-50 p-4 text-sm">
                  <div><strong>Nodos:</strong> 5</div>
                  <div><strong>Aristas:</strong> 6</div>
                  <div><strong>Salida de Kahn:</strong> [{comparison.kahnOrder.join(", ")}]</div>
                  <div><strong>Salida de DFS:</strong> [{comparison.dfsOrder.join(", ")}]</div>
                </div>
              </div>
            </CardContent>
          </Card>
        </motion.div>

        <SummaryPanel />

        <Tabs defaultValue="kahn" className="space-y-6">
          <TabsList className="grid w-full grid-cols-2 rounded-2xl">
            <TabsTrigger value="kahn">Algoritmo de Kahn</TabsTrigger>
            <TabsTrigger value="dfs">TopSort con DFS</TabsTrigger>
          </TabsList>

          <TabsContent value="kahn">
            <AlgorithmTab mode="kahn" steps={kahnSteps} code={pythonKahn} />
          </TabsContent>

          <TabsContent value="dfs">
            <AlgorithmTab mode="dfs" steps={dfsSteps} code={pythonDFS} />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
