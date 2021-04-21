import { useState } from 'react';

const DEFER_TIME = 500;

export function useDebounce() {
  const setTimer = useState<number | null>(null)[1];

  function debounce(baseFunc: () => void) {
    const newTimer = window.setTimeout(() => {
      baseFunc();
      setTimer(null);
    }, DEFER_TIME);
    setTimer(timer => {
      if (timer) window.clearTimeout(timer);
      return newTimer;
    });
  }

  function debouncePromise<T>(basePromiseFunction: () => Promise<T>): Promise<T> {
    let outResolve: (() => void) | null = null;
    const promise = new Promise((resolve: (value: unknown) => void) => {
      outResolve = () => resolve(undefined);
    });
    const newTimer = window.setTimeout(() => {
      outResolve?.();
      setTimer(null);
    }, DEFER_TIME);
    setTimer(timer => {
      if (timer) window.clearTimeout(timer);
      return newTimer;
    });
    return promise.then(basePromiseFunction);
  }

  return { debounce, debouncePromise };
}
